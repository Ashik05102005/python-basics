my_dict = {
    "name" : "Ashik" ,
    "age" : 21 ,
    "place" : "vadakara"
}
# get all keys 
key_list = []
for key in my_dict : 
    key_list.append(key)
print(key_list)

#get all values
value_list = []
for value in my_dict.values():
    value_list.append(value)
print(value_list)

#get all items (key , value)
items_list = []
for key,value in my_dict.items():
    items_list.append({"key" : key , "value" : value})
print(items_list)