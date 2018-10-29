def show():
    no = 0
    no+=1
    yield no

    no+=1
    yield no

for x in show():
    print(x)