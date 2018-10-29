
import sqlite3 as sql
conn = sql.connect("myshop.db")
print(conn)
conn.close()