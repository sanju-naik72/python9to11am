
name = input("Enter Your Name : ")
x = iter(name)
while True:
    try:
        print(next(x),end="")
    except StopIteration as si:
        break