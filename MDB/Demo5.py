uname = input("Enter username : ")
upass = input("Enter password : ")

from pymongo import MongoClient
mc = MongoClient()
ms = mc.MyShop
d1={"username":uname,"password":upass}
res = ms.login.find(d1)

if res.count() != 0:
    print("Valid User")
else:
    print("Invalid User")