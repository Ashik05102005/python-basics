def decorator (func) :
    def wrapper ():
        print("execution begins ")
        func()
        print("execution completed ")
    return wrapper

@decorator
def greet() :
    print("hello world ")

greet()