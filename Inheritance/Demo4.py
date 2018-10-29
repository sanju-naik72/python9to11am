class A:
    def assign(self,id,na):
        self.idno = id
        self.name = na

class B(A):
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)

b1 = B()
b1.assign(101,"Ravi")
b1.display()


