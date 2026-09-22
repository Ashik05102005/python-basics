num = {1, 2, 3, 4, 5, 7, 9, 10, 11, 77, 15, 16, 28} 

# remove the 11 from the set 
num.remove(11)
print(num)

# remove the 15 from the set 
num.discard(15)

# if the element is not exist no error 
num.discard(100)
print(num)

poped_num = num.pop()
print("poped_number" , poped_num)
print("set after popeed" , num)

