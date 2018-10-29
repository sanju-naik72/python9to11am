
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
print(d1)
d1.clear()
print(d1) # Empty Dict

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
val = d1.get("idno")
print(val)
val = d1.get("status")
print(val)

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
val = d1.items()
print(val)
print(type(val))

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
val = d1.values()
print(val)
print(type(val))

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
val = d1.keys()
print(val)
print(type(val))

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
val = d1.pop("idno")
print(val)
print(d1)

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
val = d1.popitem()
print(val)
print(d1)

print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
print(d1)
d1["status"] = True
print(d1)
d1.setdefault("designation")
print(d1)
val = d1.setdefault("status")
print(val)










