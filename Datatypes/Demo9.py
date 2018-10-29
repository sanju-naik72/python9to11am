
t1 = 10
print(t1) # 10
print(type(t1)) # <class 'int'>

print("--------------------------")

t1 = 10,20.25,"sathya",True # packing
print(t1)
print(type(t1))

a,b,c,d = t1  # unpacking
print(a,type(a)) # 10  <class 'int'>
print(b,type(b)) # 20.25  <class 'float'>
print(c,type(c)) # Sathya  <class 'str'>
print(d,type(d)) # True  <class 'bool'>


print("------------------")

t2 = (10,)
print(t2)
print(type(t2))


