class EvenIter:
    def __init__(self,max=0):
        self.max = max-1
    def __iter__(self):
        self.no = 0
        return self
    def __next__(self):
        if self.no < self.max:
            self.no+=2
            return self.no
        else:
            raise StopIteration

no = int(input("Enter No : "))
for x in EvenIter(no):
    print(x)