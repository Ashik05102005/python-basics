num1 = {1,2,3}
num2 = {4,5,6}
num3 = {7,8,9}
num4 = {2,3,4}

# compains num1 set and num2 (union)
res = num1.union(num2)
print(res)

# compains res set and num3 (union)
res = res|num3
print(res)

# return elements which is common in both sets 
inter = num1.intersection(num4)
print(inter)

# return elements which is common in both sets 
inter = num2 & num4
print(inter)

#return elements in the first set and not in seccond
diff = num1.difference(num4)
print(diff)

#return elements in the first set and not in seccond
diff = num2 - num4
print(diff)



