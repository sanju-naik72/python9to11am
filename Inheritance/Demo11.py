
class First:
    def calc(self,no1,no2):
        print("Add = ",no1+no2)
        print("Sub = ",no1-no2)

class Second(First):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print("Mul = ", no1 * no2)
        print("Div = ", no1 / no2)

class Three(Second):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print("Mod = ", no1 % no2)
        print("Fllor Div = ", no1 // no2)


t1 = Three()
t1.calc(10,2)



