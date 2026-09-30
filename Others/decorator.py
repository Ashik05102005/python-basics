def decorator (func) :
    def wrapper ():
        print("Function is not working properly")  
    return wrapper

@decorator
def greet() :
    print("hello world ")
    
greet()