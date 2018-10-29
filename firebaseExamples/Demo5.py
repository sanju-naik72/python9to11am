
# Example Program to Read all Details of 1 Product

from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://pyfbsample.firebaseio.com/Merchant/",None)
pno = int(input("Enter Product No : "))
d1 = fire.get("stock",pno)
if d1 == None:
    print("No Product Available")
else:
    print(d1)