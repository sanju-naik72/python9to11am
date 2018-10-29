
class MyIter:
    def __init__(self,max=0):
        self.max = max
    def __iter__(self):
        self.no = 0
        return self
    def __next__(self):
        if self.max > self.no:
            self.no+=1
            return self.no
        else:
            raise StopIteration

my = MyIter(3)
my1 = iter(my)
print(next(my1))
print(next(my1))
print(next(my1))
print(next(my1))

#While loop
no = int(input("Enter a No : "))
my = MyIter(no)
my1 = iter(my)
while True:
    try:
        print(next(my1))
    except:
        break


no = int(input("Enter a No : "))
for x in MyIter(no):
    print(x)