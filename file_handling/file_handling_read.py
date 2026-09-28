
file = open("file_handling/data.txt" , "r")
# read and print 5 elements in python 
# print(file.read(5))

# print(file.readline())
# print(file.readline())
# print(file.readline())

content = file.readlines()

print(content)

file.close()