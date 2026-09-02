# 15. Polymorphism (Function Overriding)

class BankAccount:
    def return_name(self):
        print("Bank Account")

class SavingAccount(BankAccount):
    def return_name(self):
        print("Saving Account")

sv = SavingAccount()

sv.return_name()