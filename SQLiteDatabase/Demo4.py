import sqlite3 as sql
conn = sql.connect("myshop.db")
curs = conn.cursor()
try:
    curs.execute("insert into product values (102,'OPPO',185000.00)")
    print("Product Inserted")
except sql.IntegrityError as ie:
    print(ie)
    print("Product No available")
finally:
    curs.close()
    conn.commit()
    conn.close()
    print("Thanks")
