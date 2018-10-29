# Using for loop on a File Object

f = open("sample.txt","r")
for x in f:
    print(x)

f.close() # File Closed
