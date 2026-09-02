# Assignment Problem

# 1. Create a BankAccount class with attributes account_number, owner_name, and balance. Add methods to depost, withdraw and check balance.
'''
class BankAccount:
    def __init__(
            self, 
            account_number, 
            owner_name, 
            balance
        ):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = float(balance)
    
    def deposit(self, amount):
        if float(amount) > 0:
            self.balance += float(amount)
            print(f"{amount} credited in your account.")
        else:
            print("Transaction Failed, Please try again...")
    
    def withdraw(self, amount):
        if self.balance >= float(amount) and float(amount) > 0:
            self.balance -= float(amount)
            print(f"{amount} debited from your account.")
        else:
            print("Insuffiecient balance, Please try again...")
    
    def check_balance(self):
        print(f"Available Balance: {self.balance}")

BA1 = BankAccount("BA0001", "Avanit Kumar", 85000)

BA1.check_balance()
BA1.deposit(5000)
BA1.check_balance()
BA1.withdraw(100000)
BA1.check_balance()
BA1.withdraw(100)
BA1.check_balance()
'''

# 2. Create a class Book with the following attributes: title, author, list of reviews and add methods to: add a new new review, count review, display all reviews.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.review_list = []

    def add_new_review(self, new_review):
        self.review_list.append(new_review)
        print(f"Review added successfully...")
    
    def count_review(self):
        print(f"Total review count: {len(self.review_list)}")

    def display_all_review(self):
        for review in self.review_list:
            print(self.review_list)

b1 = Book("Python fundamentals", "Cipher Mind")

b1.add_new_review("Great book to start.")

b1.count_review()

b1.display_all_review()


b2 = Book("Destination", "Mark Lock")

b2.add_new_review("Fun to read.")

b2.count_review()

b2.display_all_review()
'''

# 3. Create a class Student with private attributes __name, __roll_no, and __marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 and name can not be empty).

'''
class Student:

    def __init__(self, name, roll_no, marks):
        self.set_info(name, roll_no, marks)
    def set_info(self, name, roll_no, marks):
        if name.strip() != "":
            self.__name = name
        else:
            print("Name is not valid, Try again")
        if roll_no not in range(1, 101):
            print("Roll number must be in 1 to 100")
        else:
            self.__roll_no = roll_no
        if marks < 0 or marks > 100:
            print("Wrong marks")
        else:
            self.__marks = marks
    def get_info(self):
        print(f"Name: {self.__name}\nRoll No: {self.__roll_no}\nMarks: {self.__marks}")
        

s1 = Student("Avanit Kumar", 23, 98)

s1.get_info()
'''

# 4. Create a class Shape with a methode area(). Create subclasses Circle, Rectangle, and Triangle that override the area() method.
'''
class Shape:
    def area(self):
        print("Area of the shape")

class Circle(Shape):
    def area(self):
        print("Area of Circle")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")

class Triangle(Shape):
    def area(self):
        print("Area of Triangle")

c = Circle()

c.area()

r = Rectangle()

r.area()

t = Triangle()

t.area()
'''

# 5. Create a base class Vehicle with attributes like brand and model. Create two subclasses Car and Bike that add extra attributes - seats(in car) & engine_cc (in Bike).
'''
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seat):
        super().__init__(brand, model)
        self.seat = seat

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

c = Car("Duster", "D001", 5)

b = Bike("Yamaha", "Y001", 200)

print(f"Car Name: {c.brand}\nCar Model: {c.model}\nTotal Seat: {c.seat}")

print(f"Bike Name: {b.brand}\nBike Model: {b.model}\nEngine Power: {b.engine_cc}")
'''
# 6. Create a Abstract class Employee with an abstract method calculate_salary(). Create subclasses Intern, FullTimeEmployee and ContractEmployee that implement the method differently.
'''
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("Salary of Intern")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary of Full Time Employee")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Salary of Contract Employee")

i = Intern()
fte = FullTimeEmployee()
ce = ContractEmployee()

i.calculate_salary()
fte.calculate_salary()
ce.calculate_salary()
'''
# 7. Create a class Person that follows the constructor to work with: name only, name + age, name + age + address. As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.
'''
class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address


p1 = Person("Avanit Kumar", 22, "Rajastha, India")

print(f"Person Name: {p1.name}\nAge: {p1.age}\nAddress: {p1.address}")
'''

# 8. Create a class Player with: a class variable player_count instance variables name and level Track how many players were created.
'''
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.set_player_count()
        
    def set_player_count(self):
        Player.player_count += 1

    @classmethod
    def count_player(self):
        print(f"Total Player: {self.player_count}")

p1 = Player("Avanit Kumar", 8)

p2 = Player("Rohan Sharma", 7)

p3 = Player("Mona Roy", 3)

Player.count_player()
'''

# 9. Create the following classes: Herbivore, Carnivore, Omnivore with some attributes & methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.
'''
class Herbivore:
    def __init__(self):
        self.favorite_plant = "Berries"
        self.eating_speed = "Slow"

    def eat_plants(self):
        print(f"Bear eats {self.favorite_plant}")


class Carnivore:
    def __init__(self):
        self.favorite_prey = "Fish"
        self.hunting_speed = "Fast"

    def hunt(self):
        print(f"Bear hunts {self.favorite_prey}")


class Omnivore:
    def __init__(self):
        self.plant_food = "Fruits"
        self.meat_food = "Fish"

    def eat_both(self):
        print(f"Bear eats {self.plant_food} and {self.meat_food}")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)


bear = Bear()

print(bear.favorite_plant)
print(bear.favorite_prey)
print(bear.plant_food)
print(bear.meat_food)

bear.eat_plants()
bear.hunt()
bear.eat_both()
'''

# 10. Mini Project - OOP Chat System Let's create a Chat System using OOPs concepts. We have to create classes: User, Message ChatRoom And we have to implement functions: sending messages, viewing chat history & user joining and leaving the chatroom.
import time


class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def join_chat(self, chatroom):
        chatroom.add_user(self)

    def leave_chatroom(self, chatroom):
        chatroom.remove_user(self)

    def send_message(self, chatroom, content):
        chatroom.send_message(self, content)


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = time.ctime()

    def display_message(self):
        print(f"[{self.timestamp}] {self.sender.username}: {self.content}")


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.username} joined {self.room_name}.")
        else:
            print(f"{user.username} is already in the room.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left {self.room_name}.")
        else:
            print(f"{user.username} is not in the room.")

    def send_message(self, sender, content):
        if sender in self.users:
            message = Message(sender, content)
            self.messages.append(message)
            print(f"{sender.username} sent a message.")
        else:
            print(f"{sender.username} must join the room first.")

    def view_history(self):
        print(f"\n--- Chat History: {self.room_name} ---")

        if not self.messages:
            print("No messages yet.")
            return

        for message in self.messages:
            message.display_message()


user1 = User("Avanit", 101)
user2 = User("Rahul", 102)

room = ChatRoom("Python OOP")


user1.join_chat(room)
user2.join_chat(room)

user1.send_message(room, "Hello everyone!")
user2.send_message(room, "Hi Avanit!")
user1.send_message(room, "We are learning OOP.")


room.view_history()


user2.leave_chatroom(room)

user2.send_message(room, "I have left the room.")