def sample():
    print("I am sample function")
    class Fun:
        def m1(self):
            print("I am Fun class method")
    f = Fun()
    return f

f1 = sample()
f1.m1()

