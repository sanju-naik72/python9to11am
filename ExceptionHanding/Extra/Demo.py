
from ExceptionHanding.Extra.validation import validateAge
try:
    age = int(input("Enter age : "))
    res = validateAge(age)
    print(res)
    cno = int(input("Enter Contact No : "))
except ValueError as ve:
    print(ve)
