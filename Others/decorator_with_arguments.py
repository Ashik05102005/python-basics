def decorator(func):
    def wrapper(*args , **kwargs):
        print("function starts")
        res = func(*args , **kwargs)
        print("function starts")
        return res
    return wrapper

@decorator
def add(a,b):
    return a+b

print(add(5,7))




