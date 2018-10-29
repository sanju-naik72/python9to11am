class Employee:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("destructor")

e1 = Employee()
del e1
