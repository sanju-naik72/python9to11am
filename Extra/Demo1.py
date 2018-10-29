class Wish:
    @staticmethod
    def common():
        print("Hello Every One !")

    @classmethod
    def diffrent(cls):
        if cls.__name__ == "She":
            print("Welcome Miss")
        elif cls.__name__ == "He":
            print("Welcome Mr ")
        else:
            print("Welcome")
#------------------------------------
class He(Wish):
    def show(self):
        print("I am He Class")

class She(Wish):
    def show(self):
        print("I am She Class")

h1 = He()
h1.show() # instance method
h1.common() # Static Method
h1.diffrent() # Class Method
print("------------------------")
s1 = She()
s1.show() # instance method
s1.common() # static method
s1.diffrent() # class method
print("------------------------")
# Calling With Class Name
Wish.diffrent()
He.diffrent()
She.diffrent()


