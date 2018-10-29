
from pymongo import MongoClient
mc = MongoClient()
ms = mc.MyShop
no = int(input("Enter Product No : "))
d1 = {"pno":no}
res = ms.Product.find(d1)
if res == None:
    print("ok")
for x in res:
    for k,v in x.items():
        print(k," : ",v)