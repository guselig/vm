import streamlit as st
import pyodbc
import pandas as pd

def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["database"]["server"]
        + ";DATABASE="
        + st.secrets["database"]["database"]
        + ";UID="
        + st.secrets["database"]["username"]
        + ";PWD="
        + st.secrets["database"]["password"]
    )

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        # Usando pandas para ler os resultados do query diretamente em um DataFrame
        return pd.read_sql_query(query, conn)

rows = run_query("SELECT * FROM Equipments;")

# Usando st.dataframe para exibir o DataFrame no Streamlit
st.dataframe(rows)
