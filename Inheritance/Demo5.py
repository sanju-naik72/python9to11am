class A:
    def __init__(self):
        print("Default const of Class A")

class B(A):
    def show(self):
        print("Show of B")

b1 = B()
b1.show()