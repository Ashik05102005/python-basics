
class student : 
    #class or static variables 
    school = "ABCD school"

    def __init__(self , name ):
        # instance variable (with self )
        self.name = name 

    def greet(self):
        #local variable 
        msg = "Welcome"
        print(f"{msg} {self.name}".upper())

student1 = student("Ashik")
student2 = student("Rahul")
print(student1.name)
print(student1.school)
student1.greet()

print("_____________\n")

print(student2.name)
print(student2.school)
student2.greet()