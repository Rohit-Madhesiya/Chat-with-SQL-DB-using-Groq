import sqlite3


# connection to sqlite
connection=sqlite3.connect("student-db")

# create a cursor object to insert record, and create table
cursor=connection.cursor()

# create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),
                    CLASS VARCHAR(25),
                    SECTION VARCHAR(25),
                    MARKS INT)
"""

cursor.execute(table_info)

# insert records
cursor.execute('''Insert into STUDENT values('Rohit','GenAI','B',86)''')
cursor.execute('''Insert into STUDENT values('Rahul','ML','A',60)''')
cursor.execute('''Insert into STUDENT values('Ankit','Java','A',90)''')
cursor.execute('''Insert into STUDENT values('Abhi','SpringBot','B',70)''')
cursor.execute('''Insert into STUDENT values('Anubhav','Python','C',30)''')
cursor.execute('''Insert into STUDENT values('Aryan','Kafka','B',65)''')

# display the records
print("The inserted records are----")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
  print(row)

# commit changes in database
connection.commit()
connection.close()