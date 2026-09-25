
class student : 
    def __init__(self,name , age ):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Welcome {self.name.upper()}")

std1 = student("Ashik" , 21)
std2 = student("rahul" , 22)

print(std1.name , std1.age )
std1.greet()
print(std2.name , std2.age) 
std2.greet()