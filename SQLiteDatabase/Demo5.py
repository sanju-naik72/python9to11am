import sqlite3 as sql
conn = sql.connect("myshop.db")
curs = conn.cursor()

try:
    pno = int(input("Product No : "))
    pname = input("Product Name : ")
    pprice = float(input("Product Price : "))
    curs.execute("insert into product values (?,?,?)",(pno,pname,pprice))
    print(pno," Product is Inserted")
except ValueError as ve:
    print("Wrong Input")
except sql.IntegrityError as ie:
    print(ie)
finally:
    curs.close()
    conn.commit()
    conn.close()
    print("Thanks")
