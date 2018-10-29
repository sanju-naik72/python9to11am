
from pymongo import MongoClient
mc = MongoClient()
ms = mc.MyShop
res = ms.Product.find()

for x in res:
    for key,value in x.items():
        print(key,"---",value)

