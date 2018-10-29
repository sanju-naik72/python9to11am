class MultiIter:
    def __init__(self,max=0):
        self.max = max

    def __iter__(self):
        self.no = 1
        return self

    def __next__(self):
        if self.max > self.no:
            self.no*=2
            return self.no
        else:
            raise StopIteration

# m = MultiIter(5)
# i = iter(m)
# print(next(i)) # 2
# print(next(i)) # 4
# print(next(i)) # 8
# print(next(i)) # EXCEPTION

# no = int(input("Enter No : "))
# # m = MultiIter(no)
# # i = iter(m)
# # while True:
# #     try:
# #         print(next(i))
# #     except:
# #         break

no = int(input("Enter No : "))
for x in MultiIter(no):
    print("-----> ",x)
