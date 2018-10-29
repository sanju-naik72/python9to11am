no1 = int(input("1st No : "))
no2 = int(input("2nd No : "))
print("The sum = ",no1+no2)

try:
    print("The Div = ",no1/no2)   
except ZeroDivisionError:
    print("Invaid 2nd Input")
    
print("The Mul = ",no1*no2)
print("The Sub = ",no1-no2)
print("Thanks")
