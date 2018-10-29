class Employee:
    comp_name = "sathya"
    comp_cno = 9052492329
    def display(self):
        print("Employee Details")
        print(Employee.comp_name)
        print(Employee.comp_cno)

e1 = Employee()
e1.display()
print(Employee.comp_name)
print(Employee.comp_cno)
print(e1.comp_name)
print(e1.comp_cno)





