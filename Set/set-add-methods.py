num = {1,2,5,3,4,2,1}
print(num)

# add a value 7 , 7 is not in the set so add the number 7 to set 
num.add(7)
print(num)

# 4 is already exist on there so it set doesnt change 
num.add(4)
print(num)


# update
# used to add multiple values in to set 
num.update([9,10,11])
print(num)

# we can use set also
newSet = {16,15,77,28}
num.update(newSet)
print("after add the set")
print(num)
