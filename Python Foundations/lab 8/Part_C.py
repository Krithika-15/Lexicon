class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

savings_1 = SavingsAccount("Harry", 10000, 0.025)
savings_2 = SavingsAccount("John", 5000, 0.015)

for account in [savings_1, savings_2]:
    print(f"Owner : {account.owner}\nBalance : {account.balance}\nInterest Rate : {account.interest_rate}\n")

#SavingsAccount is an Account, because every savings account has owner and balance
#SavingsAccount also has its own attribute interest_rate

print("savings object is an Account (Parent class) ?")
print(isinstance(savings_1, Account))
print("savings object is a SavingsAccount (child class) ?")
print(isinstance(savings_1, SavingsAccount))
