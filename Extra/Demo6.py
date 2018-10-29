
def outer_fun():
    print("I am outer function")
    def inner_fun():
        print("I am inner function")
    inner_fun()

outer_fun()