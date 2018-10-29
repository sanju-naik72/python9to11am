
import re
s1 = "This is Naveen"
name = input("Enter Your Name : ")
res = re.match(name,s1)
print(res)
print(type(res))
print(res.group())