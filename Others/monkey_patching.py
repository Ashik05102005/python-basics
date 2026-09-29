# class Student :
#     def __init__(self, name):
#         self.name = name 

#     def greet(self):
#         print("welcome " , self.name)


# def new_greet():
#     print("Welcome")

# student1 = Student("Ashik")
# student1.greet()

# student1.greet=new_greet

# student1.greet()

class Payment :
    def pay(self):
        print("Payment sucess full")

def test_pay ():
    print("fake payment")

payment = Payment()

payment.pay()

payment.pay = test_pay

payment.pay()

