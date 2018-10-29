class Employee:
    comp_name = "sathya" # static variable
    @staticmethod
    def show():
        print("I am Static method")
    @classmethod
    def printcls(cls):
        print("I am Class Method")

    def display(self):
        print(self.comp_name) # calling static variable
        self.show() # calling static method
        self.printcls() # calling class method

e1 = Employee()
e1.display()