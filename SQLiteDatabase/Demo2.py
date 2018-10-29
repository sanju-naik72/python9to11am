
import sqlite3 as sql
conn = sql.connect(r"C:\Users\android\Desktop\myshop.db")
print(conn)
conn.close()