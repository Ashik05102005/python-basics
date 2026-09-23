
my_dict = {
    "name" : "Ashik" ,
    "age" : 21 ,
    "place" : "vadakara"
}
print(my_dict)

# access dictionary by using get()
print(my_dict.get("place"))

# acessing dictionary by using []
print(my_dict["name"])

# add data key-value pair by using []
my_dict["country"] = "india"
print(my_dict)

# update using []
my_dict["age"] = 22
print(my_dict)