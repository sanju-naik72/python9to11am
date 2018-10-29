class A:
    def method_A(self):
        print("A class Method")

class B:
    def method_B(self):
        print("B class Method")

class Outer(A):
    def m1(self):
        print("Outer class m1")

    class Inner(B):
        def m2(self):
            print("Inner class m2")

o = Outer()
o.m1()
o.method_A()

i = o.Inner()
i.m2()
i.method_B()