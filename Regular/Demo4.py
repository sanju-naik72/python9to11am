
import re
s1 = "This is sathya and This is python"
word = input("Enter a Word to Find : ")
res = re.findall(word,s1)
if res == []:
    print("No Match Found")
else:
    print(res)
