
import re
s1 = "This is sathya and This is python"
word = input("Enter a Word to Search :")
res = re.search(word,s1)
print(res)
print(type(res))
print(res.group())
print(res.start())
print(res.end())
