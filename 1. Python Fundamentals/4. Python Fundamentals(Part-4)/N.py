# 13. Types of Inheritance

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} creditted in your Account.")
        else:
            print(f"{amount} is not a valid Amount")
    
    def withdraw(self, amount):
        if self.balance > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} debited from your account.")
        else:
            print("Transaction failed.")
    
    def check_balance(self):
        print(f"Account Balance: {self.balance}")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}\nCustomer Name: {self.account_holder_name}\nAmount: {self.balance}")

class SavingAccount(BankAccount): # Single Inheritance
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        print(f"Interest: {self.balance*self.interest_rate*0.01}")
    
    def add_interest(self):
        self.balance += self.balance*self.interest_rate*0.01
    
    def withdraw(self, amount):
        if self.balance > 0 and amount <= self.balance and self.balance-amount >= 1000:
            self.balance -= amount
            print(f"{amount} debited from your account.")
        else:
            print("Transaction failed.")

class PremiumSavingsAccount(SavingAccount): # Multilevel Inheritance
    def __init__(self, account_number, account_holder_name, balance, interest_rate, minimum_balance, cashback_rate):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.minimum_balance = minimum_balance
        self.cashback_rate = cashback_rate

    def calculate_cashback(self):
        print(f"Cashback: {self.balance*self.cashback_rate*0.01}")

    def apply_premiumbenefits(self): # Comple this 
        if self.balance >= 500000:
            print()


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def overdraft():
        print("OverDraft Method")

    def checkoverdraftlimit():
        print("overdraft limit checker")

class SalaryAccount(SavingAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, employee_name, salary_amount):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.employee_name = employee_name
        self.salary_amount = salary_amount
    
    def credit_salary(self):
        print("Credit Salary Method")

    def check_salary_details(self):
        print("check salary details Method")

class Interest(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, ):
        super().__init__(account_number, account_holder_name, balance)


sv1 = SavingAccount("SA001", "Rahul Sharma", 50000, 6.5)
sv2 = SavingAccount("SA002", "Priya Rajpoot", 75000, 7.0)

sv1.display_account_details()
sv2.display_account_details()

sv2.calculate_interest()
sv2.add_interest()

sv2.display_account_details()

psv1 = PremiumSavingsAccount("PS001", "Amit Kaira", 200000, 7.5, 100000, 2)
psv2 = PremiumSavingsAccount("PS002", "Neha K", 350000, 8.0, 150000, 3)