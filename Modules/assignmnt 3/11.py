class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")
class SavingsAccount(BankAccount):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
bank_account = BankAccount(balance=100000, account_number="1234567890")
print(bank_account.balance)
print(bank_account.account_number)
bank_account.deposit(10000)
print(bank_account.balance)
bank_account.withdraw(50000)
print(bank_account.balance)
bank_account.withdraw(150000)
savings_account = SavingsAccount(balance=200000, account_number="9876543210", interest_rate=5)
print(savings_account.balance)
print(savings_account.account_number)
print(savings_account.interest_rate)
savings_account.add_interest()
print(savings_account.balance)
