
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