class Employee:
    def __init__(self,id=0,name=None,salary=0.0):
        self.idno = id
        self.name = name
        self.salary = salary

    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)
        print("SALARY = ",self.salary)

e1 = Employee()
e1.display()
print("---------------")
e2 = Employee(101)
e2.display()
print("---------------")
e3 = Employee(102,"Ravi")
e3.display()
print("---------------")
e3 = Employee(salary=125000.00,id=103)
e3.display()



