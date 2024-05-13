import streamlit as st
import pyodbc
import pandas as pd

def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

def run_query(query):
    # Aqui usamos a conexão diretamente com pandas sem criar um cursor explicitamente
    return pd.read_sql_query(query, conn)

try:
    rows = run_query("SELECT * FROM Equipments;")
    # Usando st.dataframe para exibir o DataFrame no Streamlit
    st.dataframe(rows)
except Exception as e:
    st.error("An error occurred: " + str(e))
