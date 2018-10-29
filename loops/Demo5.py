
d1 = {"idno":101,
      "name":"Ravi",
      "salary":125000.00}

# Will display only Keys and
# values in tuple format
for x in d1.items():
      print(x)
print("-------------------------")
# items method will return pair(key:value)
# as a tuple ex: ("idno":101)

for x,y in d1.items():
      print(x,y)
# In the above example unpacking tuple
# and assigning to x and y variables
print("-------------------------")




