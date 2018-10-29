from pymongo import MongoClient

print("Enter Details to Update")
pno = int(input("Product No : "))
pnam = input("Product Name : ")
pprice = float(input("Product Price : "))

mc = MongoClient()
ms = mc.MyShop
res = ms.Product.update({"_id":pno},{"$set":{"name":pnam,"price":pprice}})


