class A:
    def show(self):
        print("I am show of A")
class B:
    def display(self):
        print("I am display of B")

class C(A,B):
    def info(self):
        print("Info of C")

c1 = C()
c1.info()
c1.show()
c1.display()