# 16. Polymorphism (Duck Typing)

class SavingsAccount:
    def pay(self):
        print("Payment from savings account")


class CreditAccount:
    def pay(self):
        print("Payment using credit")

sv = SavingsAccount()

sv.pay()

cv = CreditAccount()

cv.pay()