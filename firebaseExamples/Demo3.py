from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://pyfbsample.firebaseio.com/Merchant/",None)

while True:
    pno = int(input("Enter Product No : "))
    pname = input("Enter Product Name : ")
    pprice = float(input("Enter Product Price : "))
    pqty = int(input("Enter Product Quantity : "))
    d1 = {"name":pname,"price":pprice,"quantity":pqty}
    fire.put("stock",pno,d1)
    print(pno," Product is Saved")

    ans = input("To Continue Press Y/y : ")
    if ans == "Y" or ans == 'y':
        continue
    else:
        break
print("Thanks")







