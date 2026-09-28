class Account_Management :
    def __init__(self, name , acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0

    def get_balance(self) :
        return self.balance
    
    def deposit (self , amount) :
        self.balance += amount

    def withdraw (self , amount ) :
        self.balance -= amount
    
acc1 = Account_Management("Ashik" , 100)

print(acc1.get_balance())

acc1.deposit(20000)

print(acc1.get_balance())

acc1.withdraw(5000)

print(acc1.get_balance())