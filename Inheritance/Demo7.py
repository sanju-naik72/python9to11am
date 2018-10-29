class A:
    def m1(self):
        print("m1 of Class A")

class B(A):
    def m2(self):
        print("m2 of Class B")

class C(B):
    def m3(self):
        print("m3 of Class C")

# using A class Object
a1 = A()
a1.m1()

# using B Class Object
b1 = B()
b1.m1()
b1.m2()

# using C Class object

c1 = C()
c1.m3()
c1.m2()
c1.m1()








