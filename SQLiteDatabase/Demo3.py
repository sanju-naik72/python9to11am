import sqlite3 as sql
conn = sql.connect("myshop.db")
curs = conn.cursor()
curs.execute("create table product(no number primary key,name text,price real )")
print("Table Created")
curs.close()
conn.close()
print("Thanks")