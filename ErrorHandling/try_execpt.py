
try:
    num = int(input("enter the number : "))

    res = 10/num
except ZeroDivisionError as e :  
    print("Error : " , e)

except ValueError as e :
    print("Error : " , e)
else : 
    print("Result : " , res )

finally : 
    print("Program completed ")