
num = int(input("enter the number "))
if num<2:
    print("it is not a prime number")
else:
    flag = False
    for i in range(2,num):
        if num % i ==0:
            flag = True
    if not flag:
        print("it is a prime number")
    else:
        print("it is not a prime number ")