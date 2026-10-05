class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner : {self.owner}, balance : {self.balance} SEK"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + f", interest rate : {self.interest_rate:.1%}"


account_1 = Account("Harry", 5000)
savings_account_1 = SavingsAccount("John", 6000, 0.015)

for account in [account_1, savings_account_1]:
    print(account)
