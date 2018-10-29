def outer():
    print("I am Outer")
    def inner():
        print("I am Inner")
    return inner

inn = outer()
del outer
inn()
