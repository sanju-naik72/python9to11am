
from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://pyfbsample.firebaseio.com/Merchant/",None)
pno = int(input("Enter Product No : "))
fire.delete("stock",pno)
print("Product Deleted")