class Number :
    def __init__(self,num):
        self.num = num

    def __add__(self, other):
        # print(other.num)
        return self.num+other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __eq__(self, value):
        return self.num == value.num

num1 = Number(10)
num2 = Number(20)

print("add",num1 + num2)
print("sub",num1 - num2)
print("mul",num1 * num2)
print("equal " , num1 == num2)