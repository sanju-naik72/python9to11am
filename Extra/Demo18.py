
def fun():
    a = 100
    b = 200
    c = a-b
    print(c)

f = fun
del fun
f()
fun()