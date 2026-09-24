def countdown (n):
    if(n==0):
        return 
    print(n)
    countdown(n-1)
print("count down ")
countdown(7)

print("factorial")
def factorial(n):
    # print(n)
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))       


print("fibinocci")
def fibinacci(n):
    if n<=1 : 
        return n
    # print(n-1,n-2)
    return fibinacci(n-1)+fibinacci(n-2)
print(fibinacci(5))


