import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():    # adding it as a static method,  atttribute of the class 'Account'
        """Gives back the currene time"""
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance    # using __ tells python interpreter to rewrite name in order to avoid conflict in subclass
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.name)
        print("Account created on name: {}"
              "\nAmount in your account: {}".format(name, balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            print("You added {}".format(amount))
            self.show_balance()
        else:
            print("Amount to be deposited must be greater than 0")

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
            print("You withdrew {}".format(amount))
            self.show_balance()
        elif amount <= 0:
            print("Amount to be withdrawn must be greater than 0")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"Your balance: {self.__balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:4} {} on {} (Local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    ghoul = Account('Ghoul', 0)
    print("*" * 100)

    ghoul.show_balance()
    ghoul.deposit(1000)
    ghoul.withdraw(300)
    ghoul.withdraw(1999)
    ghoul.withdraw(-19)
    ghoul.deposit(199)
    ghoul.show_transactions()

    ghoul.deposit(100)
    ghoul.show_transactions()

    ghoul.__balance = 100
    ghoul.show_balance()

    curry = Account('Stephen', 1000)
    curry.show_transactions()
    curry.__balance = 200
    curry.show_transactions()
    curry.show_balance()
    curry.deposit(1000)
    curry.__balance = 1000
    curry.show_transactions()
    # print(curry.__dict__)
    # curry._Account__balance = 200
    # curry.show_transactions()
    curry.show_balance()
    # print(curry.__dict__)
    # print()
    # print(ghoul.__dict__)
    # print()