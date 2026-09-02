# 14. Abstraction

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingAccount(BankAccount):
    def calculate_interest(self):
        print("Calculted Interest")

sv = SavingAccount()

sv.calculate_interest()