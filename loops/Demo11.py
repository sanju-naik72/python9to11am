
no = int(input("Enter a No : "))
r = no%10
no = no//10
r1 = 0
while no!=0:
    r1 = no % 10
    no = no // 10

print("Total = ",(r+r1))

