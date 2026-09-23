text = "abc"
digits = "123"
al_num = "Abc123"
upper_text = "ABC"
lower_text = "abc"
white_space = "  "

# check all elements is alphabets or letters
print(text.isalpha())

# check all elements is digits (0-9)
print(digits.isdigit())

# check the all element are alphabets or digits 
print(al_num.isalnum())

# check there only white spaces 
print(white_space.isspace())

# check all elements are uppercase 
print(upper_text.isupper())

# check all elements are lowercase
print(lower_text.islower())