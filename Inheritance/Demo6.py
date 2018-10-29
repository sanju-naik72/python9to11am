class A:
    def __init__(self):
        print("Default Const of A")
    def __del__(self):
        print("Des of Class A")

class B(A):
    def show(self):
        print("Show")

b1 = B()
b1.show()