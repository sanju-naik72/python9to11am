class MultiIter:
    def __iter__(self):
        self.no = 1
        return self
    def __next__(self):
        self.no*=2
        return self.no

for x in MultiIter():
    print(x)
