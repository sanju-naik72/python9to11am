import sqlite3 as sql
conn = sql.connect("myshop.db")
curs = conn.cursor()
curs.execute("select * from product")
li = curs.fetchall()
if li == []:
    print("No Products available")
else:
    for x in li:
        print(x)
print("Thanks")