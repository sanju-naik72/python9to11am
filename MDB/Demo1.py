
from pymongo import MongoClient
mc = MongoClient()
ms = mc.MyShop
d1 = {"pno":101,"pname":"Samsung","pprice":12500.00}
ms.Product.insert(d1)
print("Data Inserted")
