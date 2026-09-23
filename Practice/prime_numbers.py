
num = int(input("enter the number "))
res = []
for i in range (2,num+1):
    flag = False
    for j in range(2,num):
        if i!=j:
            if i % j == 0 :
                flag = True
    print(i ,flag)
    if not flag:
        res.append(i)
print(res)

