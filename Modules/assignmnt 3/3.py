class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
    def check_balance(self):
        return self.balance
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_account_number(self):
        return self.account_number
    def set_account_number(self, account_number):
        self.account_number = account_number
bank_account = BankAccount(name="Kavya", account_number="1234567890", balance=100000)
print("Name:", bank_account.get_name())
bank_account.set_name("Kavya")
print("Name:", bank_account.get_name())
print("Account Number:", bank_account.get_account_number())
bank_account.set_account_number("0987654321")
print("Account Number:", bank_account.get_account_number())
bank_account.deposit(45000)
print("Balance:", bank_account.check_balance())
bank_account.withdraw(15000)
print("Balance:", bank_account.check_balance())
