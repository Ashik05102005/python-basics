# 1)  numbers = [1,2,3,2,3]
# new_list = []
# duplicates = []
# for i in numbers :
#     if(i in new_list):
#         duplicates.append(i)
#     else :
#         new_list.append(i)
# print(duplicates)





#2) vowels = ["a" ,"e" ,"i","o","u"]
# count = 0
# str = "hello world"
# for char in str :
#     if char in vowels:
#         count +=1
# # print(count)

# 3) fruits = ["apple" , "orange ", "kiwi" ,"banana"]
# fruit_vowels = []

# for fruit in fruits :

#     if fruit[0] in vowels :
#         fruit_vowels.append(fruit)

# print(fruit_vowels)

# hello = "hello world"
# # new_hello = []
# new_hello = ''
# for i in  hello :
#     new_hello += i
#     if i in vowels :
#         new_hello+=i
        

# # print(new_hello)

str1 = "listen"  
str2 = "silent"
# flag = False
if(not len(str1)==len(str2)):
    print ("not an anagram")
else:
    count = 0
    for i in str1 :
        for j in str2 :
            if i==j :
                count+=1
            
    if(len(str1)==count):
        print("anagram")
    else :
        print("not anagramn")


string1 = "hello world i can see you"
# res = ""
# for i in string1.split():
#     res+=f"{i[0].upper()}{i[1:]} "

# print(res)

rev = ""
for i in string1.split():
    rev = f"{i} {rev}"
print(rev)
