
# Example Program to Read all Details from stock

from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://pyfbsample.firebaseio.com/Merchant/",None)
d1 = fire.get("stock",None)
print(d1)


