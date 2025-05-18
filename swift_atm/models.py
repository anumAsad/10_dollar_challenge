from datetime import datetime

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append((datetime.now(), f"Deposited ${amount}"))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append((datetime.now(), f"Withdrew ${amount}"))
            return True
        return False

    def transfer(self, amount, to_user):
        if self.balance >= amount:
            self.balance -= amount
            to_user.account.balance += amount
            self.history.append((datetime.now(), f"Transferred ${amount} to {to_user.username}"))
            to_user.account.history.append((datetime.now(), f"Received ${amount} from {self.username}"))
            return True
        return False

class User:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password  # Plain text for simplicity
        self.account = BankAccount(balance)
