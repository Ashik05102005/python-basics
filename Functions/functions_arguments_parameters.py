
# positional arguments 
def greet (name,place ):
    print(f"hello {name} from {place}")

greet("Ashik", "kkd")

# key word arguments
def fs(first,seccond):
    print(first , seccond)

fs(seccond="2nd" , first="1st")

# defualt parameters 
def add(a=5 , b=5):
    print(a+b)

add()

#---Arbitary arguments---

# *args -> used when we dont know the positional argument count at advance , store all afrguments as tuple  
def add_multiple (*numbers):
    total = 0 
    for i in numbers:
        total += i
    return total

res = add_multiple(2,5,8,7,6,3)
print(res)

# **kwargs -. used when we want to accept any number of keyword arguments , store all key word arguments as dictionary (key : value) 
def student_details(**details) : 
    print("age  = " , details['age'])

student_details(name = "Ashik"  , age = 21 , course = "python ")