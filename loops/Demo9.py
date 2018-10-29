no = int(input("Enter a No : "))
rev = 0
while no!=0:
    r = no%10
    no=no//10
    rev = r+(rev*10)

print(rev)
