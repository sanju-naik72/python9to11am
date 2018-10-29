import sqlite3 as sql
conn = sql.connect("myshop.db")
curs = conn.cursor()
try:
    pno = int(input("Product No : "))
    curs.execute("select * from product where no = ?",(pno,))
    tu = curs.fetchone()
    if tu ==  None:
        print("Invalid Product No")
    else:
        print(tu)
except ValueError:
    print("Invalid Input")
finally:
    curs.close()
    conn.close()
    print("Thanks")

