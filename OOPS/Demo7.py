class Employee:
    def display(self):
        print("I am Instance method")
        print("From Employee Class")


# Calling instance method using object
Employee().display()

# Calling instance method using object reference variable
e1 = Employee()
e1.display()

