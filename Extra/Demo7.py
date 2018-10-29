# example on iter() and next() functions
l1 = [10,20,30,40,50]
x = iter(l1)
print(next(x)) # 10
print(next(x)) # 20
print(next(x)) # 30
print(next(x)) # 40
print(next(x)) # 50
# print(next(x)) # StopIteration
