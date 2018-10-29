
import re
s1 = "Both of these issues are fixed by postponing the evaluation of annotations."
word = input("Enter a Word to Match : ")
res = re.match(word,s1)
if res == None:
    print("Match not Found")
else:
    print("Match Found")
    print(res.group())
    print(res.start())
    print(res.end())