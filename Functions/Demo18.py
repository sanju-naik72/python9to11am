def add(*a):
    res = 0
    for x in a:
        res+=x
    return res

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,30,40,50))