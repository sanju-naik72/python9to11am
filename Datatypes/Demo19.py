
s1 = {10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.difference(s2)
print(s1)
print(s2)
print(s3)
s3 = s2.difference(s1)
print(s1)
print(s2)
print(s3)
print("-------------------")
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1)
print(s2)
s1.difference_update(s2)
print(s1)
print(s2)
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.intersection(s2)
print(s1)
print(s2)
print(s3)






