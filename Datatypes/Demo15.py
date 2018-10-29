
x = [10,20,30]
print(x)
x.append(40)
print(x)
print("--------------------")

x = [10,20,30]
y = [40,50,60]
x.extend(y)
print(x)
print(y)

print("--------------------")

x = [10,20,30,40,50]
x.insert(2,154784)
print(x)
x.insert(-2,88888)
print(x)


print("--------------------")
x = [10,20,30,40,50,30,45,65]
x.remove(30)
print(x)

print("--------------------")
x = [10,20,30,40,50,30,45,65]
removed_val = x.pop(2) # 2 is +ve index
print(removed_val)
print(x)


print("--------------------")
x = [10,20,30,40,50,30,45,65]
removed_val = x.pop(-1) # -1 is -ve index
print(removed_val)
print(x)


print("--------------------")
x = [10,20,30,40,50,30,45,65]
removed_val = x.pop() # no index
print(removed_val)
print(x)

print("--------------------")
x = [10,20,30,40,50,30,45,65]
print(x)
x.clear()
print(x) # it will display Empty List


print("--------------------")
x = [10,20,30,40,50,30,45,65]
index_no = x.index(30)
print(index_no)

print("--------------------")

x = [-1,40,25,-20,89,15,16,98,-5]
print(x)
print("After Sort")
x.sort()
print(x)
print("After Reverse")
x.reverse()
print(x)








