class MyException(BaseException):
    def __init__(self, message):
        # calling super class Constructor
        super().__init__(message)




def checkAge(age):
    if age > 20:
        print("Valid Age")
    else:
        raise MyException("Invalid Age")


def checkContact(cno):
    if len(cno) == 10:
        print("Valid Contact No")
    else:
        raise MyException("Invalid Contact")


try:
    a = int(input("Enter Age : "))
    checkAge(a)
    b = input("Enter Contact No : ")
    checkContact(b)
except MyException as me:
    print(me)