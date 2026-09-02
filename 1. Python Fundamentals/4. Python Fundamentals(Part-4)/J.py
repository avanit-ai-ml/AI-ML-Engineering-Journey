# 10. Practice Problem
'''
Design & create an online store for Products (name, price). Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''

class Product:
    store_name = "Cipher Store"
    total_product = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.product_count()
    
    @classmethod
    def product_count(cls):
        cls.total_product += 1

    @staticmethod
    def discount_calculator(price, discount):
        print(f"Final Price: {price-price*discount/100}")

    def get_info(self):
        print(f"Product: {self.name} & Prrice: {self.price}")

product1 = Product("Book", 100)
product2 = Product("Cell Phone", 8000)
product3 = Product("Laptop", 90000)
product4 = Product("SSD", 18000)

print(f"Total Products: {Product.total_product}")

product3.discount_calculator(product3.price, 50)

product1.get_info()