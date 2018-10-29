
from ExceptionHanding.Extra.myexceptions import *

def validateAge(age):
    if age > 0:
        return age
    else:
        raise AgeException("Age Must Be Greater than 0")

def validateContact(cno):
    if len(cno) == 10:
        return cno
    else:
        raise ContactNoException("Contact No Must be 10digit's")


try:
    age = int(input("Enter age :"))
    print(validateAge(age))
    cno = input("Enter CNO : ")
    print(validateContact(cno))
except AgeException as ae:
    print(ae)
except ContactNoException as cne:
    print(cne)
else:
    print("Valid Details")
finally:
    print("Thanks")
