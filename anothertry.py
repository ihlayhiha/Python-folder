import datetime
import pytz


class Account:

    @staticmethod
    def _get_time():
        """Return the current local time"""
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance        # __ to prevent accidental shadowing of attributes while creating sub-classes
        self.transactions = [(Account._get_time(), balance)]
        print("Account opened on the name: {}"
        "\nAccount Balance: {}".format(name, balance))

    def show_balance(self):
        print("Your balance: {}".format(self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append((Account._get_time(), amount))
            self.show_balance()
        else:
            print("Deposit amount can only be a positive value")
    
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.transactions.append((Account._get_time(), -amount))
            self.show_balance()
        else:
            print(f"Withdrawl amount of {amount} is not possible. Either insufficient funds or input error.")
    
    def show_transactions(self):
        for date, amount in self.transactions:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrew"
                amount * -1
            print(f"{amount:4} {transaction_type} on {date} (Local time was {Account._get_time}")


if __name__ == '__main__':    
    yella = Account("Yella", 1000)
    yella.show_transactions()
    yella.deposit(1000)
    yella.show_transactions()
    print(yella.__dict__)
    yella.withdraw(100)
    yella.withdraw(100)
    yella.withdraw(2000)
    yella.show_transactions()
    print(yella._get_time())