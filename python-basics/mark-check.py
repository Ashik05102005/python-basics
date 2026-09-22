mark = int(input("enter the number  "))

if(not(mark>100) and not(mark<0)):
    if(mark>=90):
        print("A+")
    elif(mark>=80):
        print("A")
    elif(mark>=70):
        print("B+")
    elif(mark>=60):
        print("B")
    elif(mark>=50):
        print("C")
    elif(mark>=40):
        print("C+")
    else:
        print("failed")
else:
    # print("Invaalid Mark is Entered")
    if(mark>100):
        print("Mark is greater than 100")
    else:
        print("Mark is less than 0")
