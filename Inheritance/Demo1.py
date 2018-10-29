class A:
    def display(self):
        print("This is display")

class B(A):
    def show(self):
        print("This is show")


# Creating object to class A
a1 = A()
a1.display()
# a1.show() Error
print("------------------------")
# Creating object to class B
b1 = B()
b1.show()
b1.display()






