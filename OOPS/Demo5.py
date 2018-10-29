class Employee:
    comp_name = "sathya" # static variable
    @classmethod
    def display(cls):
        print("Class Method")
        print(cls)
        # calling static variable using cls
        print(cls.comp_name)

# calling class method
Employee.display()