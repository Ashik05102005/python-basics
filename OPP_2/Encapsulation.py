class BankAccount :
    def __init__(self,balance):
        self.__balance = balance

    def deposit (self , amount) :
        self.__balance += amount

    def get_balance (self):
        return self.__balance

bank = BankAccount(100000)

bank.deposit(5000)
print(bank.get_balance())
bank.deposit(15000)
print(bank.get_balance())


print("\n access directly on private members \n ")

print(bank._BankAccount__balance)