numbers = [10, 20, 10, 30, 10]

new_list = numbers.copy()

print(new_list)

for i in range(0,len(numbers)):
    numbers[i]=10

print(numbers)
print(new_list)