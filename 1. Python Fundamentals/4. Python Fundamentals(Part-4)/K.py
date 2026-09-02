# 11. Encapsulation in OOPs

class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, name, balance, aacount_number):
        self.name = name # public
        self.__balance = balance # private
        self._account_number = aacount_number #protected

    def get_name(self):
        return self.name
    def get_balance(self):
        return self.__balance
    def get_accoun_number(self):
        return self._account_number
    
    def set_name(self, new_name):
        self.__name = new_name
    def set_balance(self, new_balance):
        self.__balance = new_balance

account1 = BankAccount("Avanit Kumar", 85000, 30001)

'''
# Direct Access
print(account1.name)
print(account1._BankAccount__balance)
print(account1._account_number)
'''

print(account1.get_name())
print(account1.get_balance())
print(account1.get_accoun_number())

account1.set_name("Avanit Roy")
account1.set_balance(50000)

print(account1.get_name())
print(account1.get_balance())
print(account1.get_accoun_number())