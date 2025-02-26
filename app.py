import os
import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="LangChain: Chat with SQL Database")
st.title("LangChain: Chat with SQL Database")

# there might be prompt injection warning, to handle it, need to do this
# INJECTION_WARNING="""
# SQL agent can be vulnerable to prompt injection. Use a DB role with limited permissions.
# """
LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_option=["Use SQLLite3 Database - Student.db","Connect to your SQL Database"]

selected_opt=st.sidebar.radio(label="Choose the DB which you want to chat",options=radio_option)

if radio_option.index(selected_opt)==1:
  db_uri=MYSQL
  mysql_host=st.sidebar.text_input("Provide MySQL Host Name")
  mysql_user=st.sidebar.text_input("MySQL User Name")
  mysql_pass=st.sidebar.text_input("MySQL Password",type="password")
  mysql_db=st.sidebar.text_input("MySQL Database")
else:
  db_uri=LOCALDB

api_key=st.sidebar.text_input(label="GROQ API Key",type="password")

if not db_uri:
  st.info("Please enter the Database information and URI")

if not api_key:
  st.info("Plase add the GROQ API Key")

# LLM Model
llm_model=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)

# database connection
@st.cache_resource(ttl="1h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_pass=None,mysql_db=None):
  if db_uri==LOCALDB:
    db_file_path=os.path.abspath(os.path.join(os.path.dirname(__file__),"student-db"))
    st.write(f"Db path: {db_file_path}")
    st.write(f"Db exists:{os.path.exists(db_file_path)}")

    db_url=f"sqlite:///{db_file_path}"

    engine=create_engine(db_url)
    # creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro",uri=True)
    # return SQLDatabase(create_engine("sqlite:///",creator=creator))
    return SQLDatabase(engine)
  elif db_uri==MYSQL:
    if not (mysql_host and mysql_user and mysql_pass and mysql_db):
      st.error("Please provide all MySQL connection details")
      st.stop()
    return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}"))

if db_uri==MYSQL:
  db=configure_db(db_uri,mysql_host,mysql_user,mysql_pass,mysql_db)
else:
  db=configure_db(db_uri)

# Toolkit
toolkit=SQLDatabaseToolkit(db=db,llm=llm_model)

agent=create_sql_agent(
  llm=llm_model,
  toolkit=toolkit,
  verbose=True,
  agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
  st.session_state["messages"]=[{"role":"assistant","content":"How can I help you?"}]

for message in st.session_state.messages:
  st.chat_message(message["role"]).write("content")

user_query=st.chat_input(placeholder="Ask anything from the database")

if user_query:
  st.session_state.messages.append({"role":"user","content":user_query})
  st.chat_message("user").write(user_query)

  with st.chat_message("assistant"):
    streamlit_callback=StreamlitCallbackHandler(st.container())
    response=agent.invoke(input=user_query,callbacks=[streamlit_callback])
    st.session_state.messages.append({"role":"assistant","content":response})
    st.write(response)