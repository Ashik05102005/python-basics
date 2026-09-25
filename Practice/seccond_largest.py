numbers = [61,77,11,66,100,23,18,94]
# numbers = [1,2,7]

largest = numbers[1]
seccond_largest = numbers[0]
for i in numbers : 
    if largest < i :
        seccond_largest = largest
        largest = i
print(seccond_largest)