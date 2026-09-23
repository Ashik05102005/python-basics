
limit = int(input("enter the limit "))
res = [0,1]
for i in range(2,limit):
        res.append(res[i-1]+res[i-2])
print(res)