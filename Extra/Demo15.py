def evenGen(max=0):
    no=0
    while no < max-1:
        no+=2
        yield no

no = int(input("Enter No : "))
for x in evenGen(no):
    print(x)