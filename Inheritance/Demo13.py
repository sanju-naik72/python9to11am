class A:
    def m1(self):
        print("A class M1")
class B:
    def m1(self):
        print("B class M1")
class C(B,A): # The Order
    def m2(self):
        print("m2 of C")
c1 = C()
c1.m2()
c1.m1()









