def display(id=0,na=None,sal=0.0):
    print("Employee Details")
    print("IDNO = ",id)
    print("NAME = ",na)
    print("SALARY = ",sal)
    print("Thanks")

# Function Overloading
display()
display(na="kumar")
display(sal=185000.00)
display(sal=200000,id=102)
