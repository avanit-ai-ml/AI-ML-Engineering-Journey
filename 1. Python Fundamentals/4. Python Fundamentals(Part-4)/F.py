# 6. Attributes - class & instance

class BankAccount:
    bank_name = "ABC Bank"                  # class attribute

    def __init__(self, name, amount):
        self.name = name                    # instance attribute
        self.amount = amount                # instance attribute

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