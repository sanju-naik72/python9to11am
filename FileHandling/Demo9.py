
fname = input("File Name : ")
f = open(fname,"w")
mess = input("Enter Text to File :")
f.write(mess)
f.close() # Save and Close
print("Data Written to File")
