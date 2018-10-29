
try:
    f = open("sam.txt","r")
    s = f.read()
    print(s)
except FileNotFoundError as fnf:
    print(fnf)
