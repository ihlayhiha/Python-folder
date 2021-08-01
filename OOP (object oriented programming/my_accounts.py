# from _typeshed import StrPath
import datetime
import pytz


class Account:
    """make a record of bank accounts"""
    
    @staticmethod
    def _get_time():
        """gives the current time in UTC and local time"""
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transactions = [(Account._get_time(), balance)]

    def show_balance(self):
        print("Your balance is {}".format(self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append((Account._get_time(), amount))
            self.show_balance()
        else:
            print("Minimum deposit should be > 0")
        
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount