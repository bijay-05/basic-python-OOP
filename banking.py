# Parent Class : User
# Holds details about an user
# Has a function to show user details
# Child Class : Bank
# Stores details about the account balance
# stores details about the amount
# allows for deposits, withdraws, view_balance

# Parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(
            name, age, gender
        )
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance. Available balance is $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account has been updated : $", self.balance)