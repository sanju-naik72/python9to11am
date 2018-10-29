
class Outer:
    def m1(self):
        print("m1 of Outer")

    class Inner:
        def m1(self):
            print("m1 of Inner")
o = Outer()
o.m1()

i = o.Inner()
i.m1()