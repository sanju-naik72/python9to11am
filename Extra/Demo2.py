class Outer:
    def m1(self):
        print("m1 of Outer class")

    class Inner:
        def m2(self):
            print("m2 of Inner Class")

o = Outer()
o.m1()

i = o.Inner() # Creating Object to inner class
i.m2()

