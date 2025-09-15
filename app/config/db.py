import oracledb
from dotenv import load_dotenv
import os

load_dotenv()
conn = None

def open_connection():
    global conn

    if conn is None:
        conn = oracledb.connect(
            user="SCOTT",
            password=os.getenv("ORACLE_PASS"),
            dsn="localhost:1521/XEPDB1"
        )

    return conn

def close_connection():
    global conn

    if conn is not None:
        conn.close()
        conn = None
