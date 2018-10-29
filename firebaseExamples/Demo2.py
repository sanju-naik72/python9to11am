
from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://pyfbsample.firebaseio.com/Merchant/",None)

fire.put("stock",101,{"name":"Samsung","price":15000.00,"quantity":10})

print("101 Product is Saved")