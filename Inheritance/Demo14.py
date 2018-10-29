class A:
    def m1(self):
        print("A Class M1")
class B:
    def m1(self):
        print("B Class M1")
class C(B,A):
    def m1(self):
        super().m1()
        print("C Class M1")

c1 = C()
c1.m1()


