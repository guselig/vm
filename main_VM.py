import streamlit as st
import pyodbc

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
    with conn.cursor() as cur:
        cur.execute(query)
        # Usando pandas para ler os resultados do query diretamente em um DataFrame
        return pd.read_sql_query(query, conn)

rows = run_query("SELECT * FROM Equipments;")

# Usando st.dataframe para exibir o DataFrame no Streamlit
st.dataframe(rows)