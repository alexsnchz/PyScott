import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

conn = oracledb.connect(
    user="SCOTT",
    password=os.getenv("ORACLE_PASS"),
    dsn="localhost:1521/XEPDB1"
)
cursor = conn.cursor()
