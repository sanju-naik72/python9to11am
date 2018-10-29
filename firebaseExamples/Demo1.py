
from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://pyfbsample.firebaseio.com/",None)

fire.put("Merchant","admin",{"username":"admin","password":"admin"})

print("admin account is created")