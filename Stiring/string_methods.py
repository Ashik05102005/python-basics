text = "I love Python"
name = "   Ashik   "

# to upper case 
print(text.upper())

# to lower case 
print(text.lower())

#remove whitespaces from begining and ending
print(name.strip())

#replace text python -> react
new_text=text.replace("Python" , "React")
print(new_text)

#split by white spaces 
text_list = text.split()
print(text_list)

# split element by element 
new_list = list(name.strip())
print(new_list)

joined_list = "".join(new_list)
print("after join "+joined_list)