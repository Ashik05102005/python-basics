my_dict = {key : value  for key , value in [('name', 'Ashik'), ('age', 21), ('place', 'vadakara')]}
print(my_dict)

numbers = [1,2,3,4,5,6]

number_dict = {num : num*num for num in numbers}
print(number_dict)




names = ["Ashik", "Rahul", "John"]
ages = [22, 23, 21]

students = {name : age for name,age in zip(names,ages)}
print(students)

even_age = {name : age for name, age in zip(names,ages) if age%2==0}
print(even_age)
print("")
print("5 years later")
students = {name : age+5 for name,age in students.items()}
print(students)

