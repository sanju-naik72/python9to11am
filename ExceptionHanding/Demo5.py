import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
try:
    curs.execute("insert into Employee values(101)")
except sql.OperationalError as oe:
    print(oe)
finally:
    curs.close()
    conn.close()
    print("All connections closed")
print("Thanks")

