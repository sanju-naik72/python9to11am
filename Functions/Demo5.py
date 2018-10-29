a = 100 # Global Variable
def fun1():
    a = 90 # Local Variable
    print(a)

print(a)
fun1()
print(a)
