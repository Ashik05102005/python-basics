file = open('file_handling/data.txt' , 'a')
file.write("\napended string")
file.close()


with open('file_handling/data.txt','r') as new_file :
    print(new_file.read())