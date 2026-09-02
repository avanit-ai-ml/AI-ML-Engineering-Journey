# 5. Types of Constructors
'''
class BankAccount:
    def __init__(self): # default constructor
        self.bank_name = "Abc Bank"

    def create_account(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print(f"{amount} credited in your account.")
    
    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient Balance")
        else:
            self.amount -= amount
            print(f"{amount} Debited from your account.")

account1 = BankAccount()
account1.create_account("Avanit Kumar", 85000)

print(account1.bank_name)
print(account1.name)
print(account1.amount)

account1.deposit(5000)

print(account1.amount)

account1.withdraw(5000)

print(account1.amount)

account1.withdraw(900000)
'''

class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, name, amount): # parametrized constructor
        self.name = name
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print(f"{amount} credited in your account.")
    
    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient Balance")
        else:
            self.amount -= amount
            print(f"{amount} Debited from your account.")

account1 = BankAccount("Avanit Kumar", 85000)

print(account1.bank_name)
print(account1.name)
print(account1.amount)

account1.deposit(5000)

print(account1.amount)

account1.withdraw(5000)

print(account1.amount)

account1.withdraw(900000)