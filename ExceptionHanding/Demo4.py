try:
    no1 = int(input("1st No :"))
    no2 = int(input("2nd No :"))
    print("Sum = ",no1+no2)
    print("Div = ",no1/no2)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError as zde:
    print(zde)
else:
    print("Mul = ",no1*no2)
    print("Sub = ",no1-no2)
print("Thanks")