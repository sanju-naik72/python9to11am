
l1 = [1,2,3,4,5,6,7,8,9,10]

# a = (x**2 for x in l1)
# for y in a:
#     print(y)

for y in (x**2 for x in l1):
    print(y)
