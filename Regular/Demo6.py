
import re
s1 = input("Enter any String  : ")
res = re.findall(r"\w+",s1)
if res == []:
    print("No Word Found")
else:
    print(res[0])