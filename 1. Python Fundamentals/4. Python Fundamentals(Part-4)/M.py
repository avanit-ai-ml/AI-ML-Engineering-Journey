# 12. Inheritance in OOPs

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class SavingAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.interest = self.balance * 0.07


saving_account = SavingAccount("Avanit Kumar", 8000)

print(saving_account.interest)