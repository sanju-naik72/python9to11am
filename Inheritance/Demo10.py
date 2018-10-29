class Employee:
    def assing(self,id="Not assigned",name="Not assigned",sal="Not assigned"):
        self.idno = id
        self.name = name
        self.salary = sal
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)
        print("SALARY = ",self.salary)

e1 = Employee()
e1.assing() # calling without param's
e1.display()
print("-------------------")

e2 = Employee()
e2.assing(101) # calling with 1 param
e2.display()
print("-------------------")

e3 = Employee()
e3.assing(name="Ravi",sal=125000.00,id=101) # calling with all param's
e3.display()







