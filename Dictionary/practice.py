names = ["Ashik" , "Arun" , "rahul"]
ages = [21,22,23]

nums= [1,2,3,4,5,6]
res = {num : num*num for num in nums }
print(res)

res = {name : {"name" :name , "age" : age } for name,age in zip(names,ages)}
print(res)

res = {name : age if age%2 != 0 else "age is even" for name , age in zip(names,ages)}
print(res)