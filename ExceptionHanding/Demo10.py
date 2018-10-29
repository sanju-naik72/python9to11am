
class MyException(ZeroDivisionError):
    def __init__(self):
        super().__init__()


try:
    print(10/0)
except MyException as me:
    print(me)