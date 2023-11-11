'''
Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount.
Implement methods for deposit, withdrawal, and interest calculation.
'''

class Account :
    existing_id = set()
    def __init__(self, id, owner_name, balance, currency):
        if id in Account.existing_id:
            raise ValueError(f"The id {id} is already used.")
        self.id = id
        self.owner_name = owner_name
        self.balance = balance
        self.currency = currency

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_owner_name(self, owner_name):
        self.owner_name = owner_name

    def get_owner_name(self):
        return self.owner_name

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def deposit(self,amount):
        raise NotImplementedError("This method should be overridden by subclasses")

    def withdraw(self,amount):
        raise NotImplementedError("This method should be overridden by subclasses")

    def interest(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class SavingsAccount(Account):
    def __init__(self, id, owner_name, balance, currency, interest_rate):
        super().__init__(id, owner_name, balance, currency)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("You don't have enough money")
        self.balance -= amount

    def interest(self):
        self.balance += self.balance * self.interest_rate / 100
        return self.balance


class CheckingAccount(Account):
    def __init__(self, id, owner_name, balance, currency, overdraft):
        super().__init__(id, owner_name, balance, currency)
        self.overdraft = overdraft

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise ValueError("You don't have enough money")
        self.balance -= amount

    def interest(self):
        return self.balance

