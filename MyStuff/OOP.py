# Class definition for a simple calculator
class Calculator:
    # Class variable: shared among all instances
    number = 100

    # Constructor method (__init__) initializes instance variables
    def __init__(self, a, b):
        # Initialize instance variables with provided arguments
        self.firstNumber = a
        self.secondNumber = b
        print("I'm called automatically when an object is created")

    # A regular instance method that prints a simple message
    def getData(self):
        print("Executing the method")

    # Instance method that returns the sum of two instance variables and the class variable
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.number


# Creating first calculator object, constructor runs automatically
obj = Calculator(2, 3)

# Calling instance methods on the first object
obj.getData()
print(obj.Summation())  # Outputs: 105 (2+3+100)

# Creating second calculator object, constructor runs again with new values
obj2 = Calculator(4, 5)

# Calling instance methods on the second object
obj2.getData()
print(obj2.Summation())  # Outputs: 109 (4+5+100)


class User:
    temp = 0

    def __init__(self, email, name, role):
        self.name = name
        self.email = email
        self.role = role
        User.temp += 1

    def display_info(self):
        print(f"User: {self.name} | Email: {self.email} | Role: {self.role}")

    @classmethod
    def display_user_count(cls):
        print(f"Total Amount of Users: {cls.temp}")


user1 = User("carl4welps@gmail.com", "Yrik", "Moon Deity")
user2 = User("ysokurov@gmail.com", "Yarik 2", "Admin")
user3 = User("tyrellwell@ecorp.com", "Tyrell", "CTO")

user1.display_info()
user2.display_info()
user3.display_info()

User.display_user_count()

#parametrize
import pytest


