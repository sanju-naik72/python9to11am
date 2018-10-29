
f = open("sample.txt","r")
s = f.read()  # entire file

print(s)
print("----------------")


f = open("sample.txt","r")
s1 = f.read(15)  # read only 15char's
print(s1)