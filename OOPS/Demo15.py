class Employee:
    def __init__(self,id,na):
        self.idno = id
        self.name = na
    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee(101,"Ravi")
e1.display()
