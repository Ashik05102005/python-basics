num1 =  {1,7,6,2}
num2 = {3,1,6,4}


# symmetric_difference : return non common elements among two sets 
res = num1.symmetric_difference(num2)
print(res)

# also use ^ insted of symmetric_difference
res = num1 ^ num2
print(res)

num3 = {1,2}
num4 = {1,2,3,4}

# check all elements of num3 are present in num4 
res = num3.issubset(num4)
print(res)

num5 = {1,2,3,4}
num6 = {1,2,7}

# check num5 contain all elements of num6 
res = num5.issuperset(num6)
print(res)

num7 = {1,2,3}
num8 = {3,5,6}

# check num7 and num8 contains no same elements return true otherwise false
res = num7.isdisjoint(num8)
print(res)