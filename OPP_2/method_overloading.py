class Calculation :
    def add(self , a, b , c = 0 ) :
        return a+b+c
    def mul(self , *numbers):
        res=1
        for i in numbers : 
            res*=i
        return res

calc = Calculation()

print(calc.add(5,7))
print(calc.mul(1,2,3,4))