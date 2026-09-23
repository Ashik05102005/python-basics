numbers = [1,2,3,4,5,6]

# normal list comprehension
squares = [num**2 for num in numbers]
print(squares)

# using if 
even = [num for num in numbers if num%2==0]
print(even)

# using if else 
even_or_odd = ["Even" if num % 2 == 0 else "Odd" for num in numbers ]
print(even_or_odd)