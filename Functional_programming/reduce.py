from functools import reduce

nums = [1,2,3,5,7,9,3,6]

sum = reduce(lambda a,b : a+b , nums)

print(sum)