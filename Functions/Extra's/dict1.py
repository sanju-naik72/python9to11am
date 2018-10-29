d1 = {
    "idno":101,
    "name":"Ravi",
    "salary":185000.00,
    "designation":"SR-Developer"}

for x in d1:
    print(x,"----",d1[x])
print("-----------------")

for x in d1.items():
    print(x)
print("-----------------")

for x,y in d1.items():
    print(x,"-----",y)

print("-----------------")

for x in d1.values():
    print(x)
    


