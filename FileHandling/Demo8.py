
import os.path as pa
fname = input("File Name with ext : ")
res = pa.exists(fname)
if res:
    print(open(fname,"r").read())
else:
    print("File Not Available")

