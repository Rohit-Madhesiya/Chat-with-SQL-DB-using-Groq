---
title: Chat With SQL Using Groq
emoji: 🌍
colorFrom: pink
colorTo: purple
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: Search Engine with SQL using Groq LLM Model
---

# LangChain: Chat with SQL Database

This project allows users to interact with SQL databases (SQLite3 or MySQL) using a conversational AI powered by LangChain and the GROQ API. It provides an intuitive interface built with Streamlit to query databases and retrieve insights using natural language.

## Features

- **Chat with SQL Database**: Query and retrieve data using natural language.
- **Support for SQLite3 and MySQL**: Choose between a local SQLite database (`student-db`) or connect to a remote MySQL database.
- **LangChain Integration**: Uses LangChain to generate and execute SQL queries.
- **GROQ API Integration**: Utilizes the Llama3-8b-8192 model for enhanced AI interactions.
- **Streamlit UI**: Provides an easy-to-use web interface.
- **Secure API Handling**: API keys are entered securely in the sidebar.
- **Caching for Performance**: Uses Streamlit's caching mechanism to optimize database queries.

## Deployment on Hugging Face Spaces

This project is configured to run on **Hugging Face Spaces** using `streamlit` as the UI framework.

### Steps to Deploy on Hugging Face Spaces

1. Create a new **Space** on [Hugging Face Spaces](https://huggingface.co/spaces) and select `Streamlit` as the SDK.
2. Upload the following project files:
   - `app.py`
   - `sqlite.py`
   - `requirements.txt`
3. **Set Up Environment Variables**:
   - You need to manually enter your `GROQ API Key` in the Streamlit sidebar while running the app.
4. Hugging Face will automatically install dependencies from `requirements.txt` and launch the app.

## Installation & Local Setup

To run this project locally, follow these steps:

### Prerequisites

- Python 3.10
- `pip` package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Rohit-Madhesiya/Chat-with-SQL-DB-using-Groq.git
cd Chat-with-SQL-DB-using-Groq

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## Usage

1. **Select Database**: Choose either `SQLite3` or `MySQL`.
2. **Provide Credentials** (for MySQL):
   - Enter `Host`, `User`, `Password`, and `Database Name`.
3. **Enter GROQ API Key**: Required for AI-powered queries.
4. **Ask Questions**: Type natural language queries in the chatbox and get SQL-powered responses.

## File Structure

```
/
|-- app.py            # Main Streamlit application
|-- sqlite.py         # SQLite database setup script
|-- requirements.txt  # Dependencies
```

## Dependencies

The required libraries are listed in `requirements.txt`. Some key dependencies include:

- `streamlit`
- `langchain`
- `sqlalchemy`
- `langchain_groq`

## License

This project is open-source and licensed under the MIT License.

## Author

Developed by [Rohit Gupta].

