
add = lambda a,b : a+b 

print(add(5,7))

check = lambda n : "Even " if n%2==0 else "Odd"
print("7 is " ,check(7))
print("2 is ",check(2))

numbers = [1,2,3,4,5,6]

squares = list(map(lambda num : num**2 , numbers) )
print(squares)

even_or_odd = list(filter(lambda num : num %2 == 0 , numbers))
print(even_or_odd)