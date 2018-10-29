
def outerFun():
    a = 100
    print("I am Outer")
    def  inneFun():
        print("I am Inner")
        print(a)
    return inneFun

print("Before Delete")
i = outerFun()
del outerFun
print("After Delete")
i()