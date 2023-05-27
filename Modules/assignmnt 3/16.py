class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
bank_account = BankAccount(account_number="1234567890", balance=99999)
print(bank_account.get_balance())
bank_account.deposit(5000)
print(bank_account.get_balance())
bank_account.withdraw(30000)
print(bank_account.get_balance())
savings_account = SavingsAccount(account_number="7654321", balance=100000, interest_rate=0.02)
print(savings_account.get_balance())
savings_account.add_interest()
print(savings_account.get_balance())
