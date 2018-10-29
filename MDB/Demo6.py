
from pymongo import MongoClient
mc = MongoClient()
ms = mc.MyShop
while True:
    pno = int(input("Product No : "))
    pnam = input("Product Name : ")
    pprice = float(input("Product Price : "))

    d1 = {"_id":pno,"name":pnam,"price":pprice}

    ms.Product.insert(d1)

    print("Data Inserted")
    ans = int(input("To Continue press 1 : "))
    if ans == 1:
        continue
    else:
        break
print("Thanks")
