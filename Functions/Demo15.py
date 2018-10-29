def calc():
    no1 = int(input("1st No : "))
    no2 = int(input("2nd No : "))
    sum = no1+no2
    sub = no1-no2
    mul = no1*no2
    div = no1/no2
    return sum,sub,mul,div

res = calc()
print(res)
print(type(res))