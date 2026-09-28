
file = open('file_handling/data.txt','w')
file.write("hello python \n")

file.writelines(["hello\n" , "python \n","hello world"])
file.close()

