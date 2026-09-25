numbers = [61,77,11,66,100,23,18,94]
largest = numbers[0]
for index in range(1,len(numbers)) :
    if largest<numbers[index] : 
        largest = numbers[index]
print(largest)