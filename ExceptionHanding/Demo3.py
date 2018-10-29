try:
    no1 = int(input("1st No : "))
    no2 = int(input("2nd No : "))
    print("Sum = ", no1 + no2)
    try:
        print("Div = ",no1/no2)
    except ZeroDivisionError as zd:
        print(zd)
    print("Mul = ",no1*no2)
    print("Sub = ",no1-no2)
except ValueError:
    print("Only Integer values")
print("Thanks")