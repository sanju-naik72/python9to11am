class Employee:
    @staticmethod
    def show():
        print("I am static method")
    @classmethod
    def display(cls):
        print("I am class method")
        # calling static method using cls
        cls.show()

# calling Class method
Employee.display()