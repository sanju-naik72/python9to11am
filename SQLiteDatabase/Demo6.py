
import sqlite3 as sql
conn = sql.connect("myshop.db")
curs = conn.cursor()
curs.execute("select * from employee")
li = curs.fetchall()
# if li == []:
#     print("No Data")

if len(li) == 0:
    print("No data found")