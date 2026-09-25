class student :

    school  = "ABC school"
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    # isinstance method (uses self and use the data of the object) 
    def display(self) : 
        print(f"I am {self.name} at {self.age}")

    # class method work with class level data (here school)
    @classmethod
    def display_school(cls):
        print(f"School name is {cls.school}")

    # static method  does not need to access object or class 
    @staticmethod
    def add(a,b) :
        print(a+b)
    



std1 = student("Ashik" , 21 )

std1.display()
std1.display_school()
std1.add(5,7)