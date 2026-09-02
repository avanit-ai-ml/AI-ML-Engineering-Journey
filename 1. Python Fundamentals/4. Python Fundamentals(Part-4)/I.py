# 9. Static Methods

class BankAccount:
    bank_name = "ABC Bank"   

    @classmethod
    def change_bank_name(cls, bank_name):              
        cls.bank_name = bank_name   

    @staticmethod
    def is_valid_amount(amount):                    # static method
        return amount > 0            

    def __init__(self, name, amount):
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

account1.change_bank_name("DEF Bank")

print(account1.bank_name)

print(BankAccount.is_valid_amount(-500))