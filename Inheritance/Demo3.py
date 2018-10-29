class A:
    @staticmethod
    def show():
        print("A class Static Method")
class B(A):
    def dispaly(self):
        print("B class Instance method")

# Calling static method using A class
A.show()

# Calling static method using B Class
B.show()