# static variables on single inheri
class A:
    comp_name = "sathya"
    def display(self):
        print("This is display")

class B(A):
    def show(self):
        print("This is show")


# calling With class A
print(A.comp_name)

# calling With class B
print(B.comp_name)

# Calling methods
b1 = B()
b1.display()
b1.show()

