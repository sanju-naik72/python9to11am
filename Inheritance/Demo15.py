
class A:
    def m1(self):
        print("A class M1 Method")

class B(A):
    def m2(self):
        print("B class M2 Method")
    def m1(self):
        super().m1()
        print("B Class M1 Method")

class C(A):
    def m3(self):
        print("C class M3 Method")

b1 = B()
b1.m2() #
b1.m1() #

print("-----------")

c1 = C()
c1.m3()
c1.m1()
