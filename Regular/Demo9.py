
import re
email = input("Enter Email id : ")
res = re.findall(r"@",email)
print(res)