
# =================================
# Simple bank Account Class
# =================================

# This is the Bank Account Class (template for bank account instances)

class BankAccount:
    """ Creating simple bank account with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account balance created for " + self.name)

    def deposit(self, amount):  # pass amount to deposit
        if amount > 0:
            self.balance += amount  # if amount to deposit > 0, new balance = old balance + amount

    def withdraw(self, amount):  # pass amount to withdraw
        if amount > 0:
            self.balance -= amount  # if amount to withdraw > 0, new balance = old balance - amount

    def show_balance(self):  # you don't pass anything here. We just use self
        print("Balance is {}".format(self.balance))


# Now we create bank account named DylanAccount

if __name__ == "__main__":  # Note. name is always __main__ if running code where it is written. not imported

    DylanAccount = BankAccount("DylanAccount_1", 0)  # initialize it with name and balance. Balance is initially 0
    DylanAccount.show_balance()  # Show initial balance

    # Then we deposit $1000 to DylanAccount
    DylanAccount.deposit(1000)  # Give it amount $1000
    DylanAccount.show_balance()  # Now we show balance after deposit.

    # Now we withdraw $500 from DylanAccount
    DylanAccount.withdraw(500)
    DylanAccount.show_balance()  # Now we show balance after withdrawal

print("="*30)

# ============================================================================
# We can improve above code so that it prints balance automatically after every withdrawal or deposit
# And then also make sure we don't withdraw more than is available in the balance.

# We can see that the Class BankAccount encapsulates methods and variables and the "client" of the class
# does not have to worry about the details.
# NOTE: "client" is any code that uses a class

class BankAccount:
    """ Creating simple bank account with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account balance created for " + self.name)

    def deposit(self, amount):  # pass amount to deposit
        if amount > 0:
            self.balance += amount  # if amount to deposit > 0, new balance = old balance + amount
            self.show_balance()  # Shows balance here after we deposit by calling method show_balance

    def withdraw(self, amount):  # pass amount to withdraw
        if 0 < amount <= self.balance:  # if amount to withdraw is more than 0, and is less or equal to balance
            self.balance -= amount  # if amount to withdraw > 0, new balance = old balance - amount
        else:
            print("The withdrawal amount must be > 0 and no more than your account balance")
        self.show_balance()  # Then call show_balance method to show balance

    def show_balance(self):  # you don't pass anything here. We just use self
        print("Balance is {}".format(self.balance))


# Now we create bank account named DylanAccount
# DylanAccount is an instance of class BankAccount and is also a client of the Class
# DylanAccount just calls the Class "BankAccount" and does not need to know the details of the Class
# "Signature" is the definition of the name and parameters of a function or class
# So as long as a "client" does not modify the signature of the "Class", it will still work.

if __name__ == "__main__":  # Note. name is always __main__ if running code where it is written. not imported

    DylanAccount = BankAccount("DylanAccount_2", 0)  # initialize it with name and balance. Balance is initially 0
    DylanAccount.show_balance()  # Show initial balance

    # Then we deposit $1000 to DylanAccount
    DylanAccount.deposit(1000)  # Give it amount $1000
    # Now we withdraw $500 from DylanAccount
    DylanAccount.withdraw(250)


print("="*30)




# ==============================================================================
# We will add a transaction log to keep the details of deposits and withdrawals
# ==============================================================================

# We will first write code to track deposits.
# Then we will later add class method to use for both deposits and withdrawals

# Transaction log of deposits will include date/time and amount deposited
# So we will need to import "datetime" module
# We will also import "pytz" module so we can log a location and UTC time
# NOTE: pytz is not installed by default. We installed it in earlier code


import datetime
import pytz

class BankAccount:
    """ Creating simple bank account with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []   # we initialize transaction_list with an empty list
        print("Account balance created for " + self.name)

    def deposit(self, amount):  # pass amount to deposit
        if amount > 0:
            self.balance += amount  # if amount to deposit > 0, new balance = old balance + amount
            self.show_balance()  # Shows balance here after we deposit by calling method show_balance
            # we will then append "UTC time" to deposit "amount" and add it to transaction_list
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdraw(self, amount):  # pass amount to withdraw
        if 0 < amount <= self.balance:  # if amount to withdraw is more than 0, and is less or equal to balance
            self.balance -= amount  # if amount to withdraw > 0, new balance = old balance - amount
        else:
            print("The withdrawal amount must be > 0 and no more than your account balance")
        self.show_balance()  # Then call show_balance method to show balance

    def show_balance(self):  # you don't pass anything here. We just use self
        print("Balance is {}".format(self.balance))

    # Now we create "show_transactions" method

    def show_transactions(self):
        for date, amount in self.transaction_list:  # transaction list has date and amount, unpacked
            if amount > 0:  # if amount in transaction_list is more than 0
                trans_type = "deposited"  # then transaction type is deposited
            else:
                trans_type = "withdrawn"  # If amount is negative number, then transaction type is withdrawn
                amount *= -1  # we convert the new amount to positive by saying negative amount = amount x -1

            print("{:6}  {} on {} (Local time was {})".format(amount, trans_type, date, date.astimezone()))


# Now we create bank account named DylanAccount

if __name__ == "__main__":  # Note. name is always __main__ if running code where it is written. not imported

    DylanAccount = BankAccount("DylanAccount_3", 0)  # initialize it with name and balance. Balance is initially 0
    DylanAccount.show_balance()  # Show initial balance

    # Then we deposit $1000 to DylanAccount
    DylanAccount.deposit(1000)  # Give it amount $1000
    # Now we withdraw $500 from DylanAccount
    DylanAccount.withdraw(250)

    # Now we can call method "show_transactions"
    DylanAccount.show_transactions()


print("="*30)




# ==============================================================================
# Static Methods
# ==============================================================================

# We can use "static method" here so we don't repeat code for transaction_list above
# for both "withdrawal" and "deposit"

import datetime
import pytz


class BankAccount:
    """ Creating simple bank account with balance """

    # We add "static method" here. it starts with @staticmethod
    # if you CTRL + click staticmethod, you will see where it is defined
    # NOTE: definition of static method starts with _ e.g. _current_time.
    # This is convention to show it is not local to BankAccount Class

    @staticmethod
    def _current_time():  # NOTE we don't use (self) here because this is static method that does not include parameters in BankAccount
        utc_time = datetime.datetime.utcnow()  # Assigns UTC time to variable utc_time
        return pytz.utc.localize(utc_time)   # Returns localized UTC time

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []   # we initialize transaction_list with an empty list
        print("Account balance created for " + self.name)

    def deposit(self, amount):  # pass amount to deposit
        if amount > 0:
            self.balance += amount  # if amount to deposit > 0, new balance = old balance + amount
            self.show_balance()  # Shows balance here after we deposit by calling method show_balance

            # We call BankAccount._current_time here to get UTC time. Also add amount to transaction_list
            self.transaction_list.append((BankAccount._current_time(), amount))

    def withdraw(self, amount):  # pass amount to withdraw
        if 0 < amount <= self.balance:  # if amount to withdraw is more than 0, and is less or equal to balance
            self.balance -= amount  # if amount to withdraw > 0, new balance = old balance - amount

            # We call BankAccount._current_time here to get UTC time. Also add amount to transaction_list
            # NOTE: you can use self._current_tume() but it is innefficient and its better to use class name
            # NOTE: we use -amount here so the test in "show_transactions" becomes negative for withdrawals hence types withdrawn

            self.transaction_list.append((BankAccount._current_time(), -amount))
        else:
            print("The withdrawal amount must be > 0 and no more than your account balance")
        self.show_balance()  # Then call show_balance method to show balance

    def show_balance(self):  # you don't pass anything here. We just use self
        print("Balance is {}".format(self.balance))

    # Now we create "show_transactions" method

    def show_transactions(self):
        for date, amount in self.transaction_list:  # transaction list has date and amount, unpacked
            if amount > 0:  # if amount in transaction_list is more than 0
                trans_type = "deposited"  # then transaction type is deposited
            else:
                trans_type = "withdrawn"  # If amount is negative number, then transaction type is withdrawn
                amount *= -1  # we convert the new amount to positive by saying negative amount = amount x -1

            print("{:6}  {} on {} (Local time was {})".format(amount, trans_type, date, date.astimezone()))



# Now we create bank account named DylanAccount

if __name__ == "__main__":  # Note. name is always __main__ if running code where it is written. not imported

    DylanAccount = BankAccount("DylanAccount_4", 0)  # initialize it with name and balance. Balance is initially 0
    DylanAccount.show_balance()  # Show initial balance

    # Then we deposit $1000 to DylanAccount
    DylanAccount.deposit(1000)  # Give it amount $1000
    # Now we withdraw $500 from DylanAccount
    DylanAccount.withdraw(250)

    # Now we can call method "show_transactions"
    DylanAccount.show_transactions()

    # ==============================================================
    # Now we will make another account with initial balance of $800
    # ==============================================================
    print("="*20)
    MarenAccount = BankAccount("MarenAccount_1", 800)
    MarenAccount.show_balance()
    MarenAccount.deposit(100)
    MarenAccount.withdraw(200)
    MarenAccount.show_transactions()

print("="*30)

# In results from MarenAccount above, although we see Balance changing from 800, to 900 to 700
# The transaction log only shows 100 deposited and 200 withdrawn.
# It does not show initial balance of $800 as a deposit.

#   100  deposited on 2018-04-08 22:10:36.416750+00:00 (Local time was 2018-04-08 17:10:36.416750-05:00)
#   200  withdrawn on 2018-04-08 22:10:36.416750+00:00 (Local time was 2018-04-08 17:10:36.416750-05:00)

# We can include initial balance of $800 as a deposit by changing initialization under __init__
# from empty list "self.transaction_list = []" to "self.transaction_list = [(BankAccount._current_time(), balance)]"





# ==============================================================================
# Initializing self.transaction_list = []
# ==============================================================================

# We can include initial balance of $800 as a deposit by changing initialization under __init__
# from empty list "self.transaction_list = []" to "self.transaction_list = [(BankAccount._current_time(), balance)]"


import datetime
import pytz

class BankAccount:
    """ Creating simple bank account with balance """

    # We add "static method" here. it starts with @staticmethod
    # if you CTRL + click staticmethod, you will see where it is defined
    # NOTE: definition of static method starts with _ e.g. _current_time.
    # This is convention to show it is not local to BankAccount Class

    @staticmethod
    def _current_time():  # NOTE we don't use (self) here because this is static method that does not include parameters in BankAccount
        utc_time = datetime.datetime.utcnow()  # Assigns UTC time to variable utc_time
        return pytz.utc.localize(utc_time)   # Returns localized UTC time

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        # we initialize transaction_list with current time and account balance. The result shows initial $800 as a deposit.
        self.transaction_list = [(BankAccount._current_time(), balance)]
        print("Account balance created for " + self.name)

    def deposit(self, amount):  # pass amount to deposit
        if amount > 0:
            self.balance += amount  # if amount to deposit > 0, new balance = old balance + amount
            self.show_balance()  # Shows balance here after we deposit by calling method show_balance

            # We call BankAccount._current_time here to get UTC time. Also add amount to transaction_list
            self.transaction_list.append((BankAccount._current_time(), amount))

    def withdraw(self, amount):  # pass amount to withdraw
        if 0 < amount <= self.balance:  # if amount to withdraw is more than 0, and is less or equal to balance
            self.balance -= amount  # if amount to withdraw > 0, new balance = old balance - amount

            # We call BankAccount._current_time here to get UTC time. Also add amount to transaction_list
            # NOTE: you can use self._current_tume() but it is innefficient and its better to use class name
            # NOTE: we use -amount here so the test in "show_transactions" becomes negative for withdrawals hence types withdrawn

            self.transaction_list.append((BankAccount._current_time(), -amount))
        else:
            print("The withdrawal amount must be more than Zero and less than your account balance")
        self.show_balance()  # Then call show_balance method to show balance

    def show_balance(self):  # you don't pass anything here. We just use self
        print("Balance is {}".format(self.balance))

    # Now we create "show_transactions" method

    def show_transactions(self):
        for date, amount in self.transaction_list:  # transaction list has date and amount, unpacked
            if amount > 0:  # if amount in transaction_list is more than 0
                trans_type = "deposited"  # then transaction type is deposited
            else:
                trans_type = "withdrawn"  # If amount is negative number, then transaction type is withdrawn
                amount *= -1  # we convert the new amount to positive by saying negative amount = amount x -1

            print("{:6}  {} on {} (Local time was {})".format(amount, trans_type, date, date.astimezone()))


# Now we create bank account named DylanAccount

if __name__ == "__main__":  # Note. name is always __main__ if running code where it is written. not imported

    DylanAccount = BankAccount("DylanAccount_5", 0)  # initialize it with name and balance. Balance is initially 0
    DylanAccount.show_balance()  # Show initial balance

    # Then we deposit $1000 to DylanAccount
    DylanAccount.deposit(1000)  # Give it amount $1000
    # Now we withdraw $500 from DylanAccount
    DylanAccount.withdraw(250)
    DylanAccount.withdraw(700)

    # Now we can call method "show_transactions"
    DylanAccount.show_transactions()

    # ==============================================================
    # Now we will make another account with initial balance of $800
    # ==============================================================

    print("="*20)
    MarenAccount = BankAccount("MarenAccount_2", 800)
    MarenAccount.show_balance()
    MarenAccount.deposit(100)
    MarenAccount.withdraw(200)
    MarenAccount.show_transactions()


print("="*30)



# ==============================================================================
# How to prevent class attributes from being modified
# ==============================================================================

# In this case, we will go to MarenAccount and modify the balance
# We will see how to prevent client accessing BankAccount Class from directly modifying balance (or other) attribute

# First we rename all BankAccount attributes in the __init__ method (name, balance, transaction_list )
# so they start with underscore (_name, _balance, _transaction_list)
# We will change the names by refactoring them

# NOTE that even with the new names with underscore, this change does not get error from intellij => "MarenAccount._balance = 200"
# In modules, intellij would have shown error message, but with class, it is for use to remember this convention

# ============================
# _name for internal use only
# ============================

# The rule is: Attributes whose name start with a single underscore (_name), are for internal use only.
# There is nothing to prevent you from messing with them, but things will break down the road if you do that.

# ======================
# Non-Public vs Private
# ======================

# Private - means that _name are enforced as being private
# Non-Public - means _name are for private use but that is not enforced.

# ====================================
# difference between _name and __name
# ====================================
# if you rename the __init__ names to use one underscore, the attributes can still be changed by "MarenAccount._balance = 200"
# but if you rename them using two underscores, the attributes are not changed by "MarenAccount.__balance = 200"
# The reason for this is because python mangles the names of class attributes (both methods and variables) that
# start with two underscores (__name).

# We will see what is happening by printing __dict__ method. "print(MarenAccount.__dict__)"
# This is the result from __dict__

# {'_name': 'MarenAccount', '_BankAccount__balance': 700, '_transaction_list':
# [(datetime.datetime(2018, 4, 9, 17, 43, 19, 442427, tzinfo=<UTC>), 800),
# (datetime.datetime(2018, 4, 9, 17, 43, 19, 442427, tzinfo=<UTC>), 100),
# (datetime.datetime(2018, 4, 9, 17, 43, 19, 442427, tzinfo=<UTC>), -200)], '__balance': 200}

# We can see that MarenAccount has an attribute called __balance with value of 200
# This data attribute was created when we assigned a value 200 to it using "MarenAccount.__balance = 200"
# Python did not find a variable with that name in MarenAccount namespace, and also did not find it in the BankAccount Class
# So it created a new data attribute called __balance

# Second reason why python did not find the __balance attribute is there is a data attribute called _BankAccount__balance
# that has the expected value of 700.
# By adding two underscores to balance (__balance), we are asking python to perform name Mangling and it automatically
# renames the attribute to start with an underscore and the name of the class. This is done behind the scenes and our source code is unchanged.

# Whenever we refer to the attribute __balance within class BankAccount, python automatically mangles it for us
# When we use the same name outside the class BankAccount, it does not mangle it (add it to class BankAccount)
# So the attribute balance within class BankAccount is hidden so it is not accidentally changed when accessing it from outside the class

# If we want to change the attribute, we can change the mangled attribute "MarenAccount._BankAccount__balance = 40".
# When we print, we now see "Balance is 40" as is expected.

# This mechanism is intended to prevent accidental shadowing of attributes when creating subclasses.
# Although it can be used as private access to variables, this use (using __ to force private access) is discouraged
# because you can use format "MarenAccount._BankAccount__balance = 40" to access the private variables

# Remember, names are mangled if they start with double underscore and if they end with no more than a single underscore


import datetime
import pytz

class BankAccount:
    """ Creating simple bank account with balance """

    # We add "static method" here. it starts with @staticmethod
    # if you CTRL + click staticmethod, you will see where it is defined
    # NOTE: definition of static method starts with _ e.g. _current_time.
    # This is convention to show it is not local to BankAccount Class

    @staticmethod
    def _current_time():  # NOTE we don't use (self) here because this is static method that does not include parameters in BankAccount
        utc_time = datetime.datetime.utcnow()  # Assigns UTC time to variable utc_time
        return pytz.utc.localize(utc_time)   # Returns localized UTC time

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        # we initialize transaction_list with current time and account balance. The result shows initial $800 as a deposit.
        self._transaction_list = [(BankAccount._current_time(), balance)]
        print("Account balance created for " + self._name)

    def deposit(self, amount):  # pass amount to deposit
        if amount > 0:
            self.__balance += amount  # if amount to deposit > 0, new balance = old balance + amount
            self.show_balance()  # Shows balance here after we deposit by calling method show_balance

            # We call BankAccount._current_time here to get UTC time. Also add amount to transaction_list
            self._transaction_list.append((BankAccount._current_time(), amount))

    def withdraw(self, amount):  # pass amount to withdraw
        if 0 < amount <= self.__balance:  # if amount to withdraw is more than 0, and is less or equal to balance
            self.__balance -= amount  # if amount to withdraw > 0, new balance = old balance - amount

            # We call BankAccount._current_time here to get UTC time. Also add amount to transaction_list
            # NOTE: you can use self._current_tume() but it is innefficient and its better to use class name
            # NOTE: we use -amount here so the test in "show_transactions" becomes negative for withdrawals hence types withdrawn

            self._transaction_list.append((BankAccount._current_time(), -amount))
        else:
            print("The withdrawal amount must be more than Zero and less than your account balance")
        self.show_balance()  # Then call show_balance method to show balance

    def show_balance(self):  # you don't pass anything here. We just use self
        print("Balance is {}".format(self.__balance))

    # Now we create "show_transactions" method

    def show_transactions(self):
        for date, amount in self._transaction_list:  # transaction list has date and amount, unpacked
            if amount > 0:  # if amount in transaction_list is more than 0
                trans_type = "deposited"  # then transaction type is deposited
            else:
                trans_type = "withdrawn"  # If amount is negative number, then transaction type is withdrawn
                amount *= -1  # we convert the new amount to positive by saying negative amount = amount x -1

            print("{:6}  {} on {} (Local time was {})".format(amount, trans_type, date, date.astimezone()))


# Now we create bank account named DylanAccount

if __name__ == "__main__":  # Note. name is always __main__ if running code where it is written. not imported

    DylanAccount = BankAccount("DylanAccount_6", 0)  # initialize it with name and balance. Balance is initially 0
    DylanAccount.show_balance()  # Show initial balance

    # Then we deposit $1000 to DylanAccount
    DylanAccount.deposit(1000)  # Give it amount $1000
    # Now we withdraw $500 from DylanAccount
    DylanAccount.withdraw(250)
    DylanAccount.withdraw(700)

    # Now we can call method "show_transactions"
    DylanAccount.show_transactions()

    # ==============================================================
    # Now we will make another account with initial balance of $800
    # ==============================================================

    # if we modify balance to $200, we see balances don't match transaction history

    print("="*20)
    MarenAccount = BankAccount("MarenAccount_3", 800)
    MarenAccount.show_balance()
    MarenAccount.__balance = 200  # We modify MarenAccount Balance to $200 here
    MarenAccount.show_balance()
    MarenAccount.deposit(100)
    MarenAccount.withdraw(200)  # We see balance here is $100 due to the modification we made above.
    MarenAccount.show_transactions()
    print(MarenAccount.__dict__)
    MarenAccount._BankAccount__balance = 40  # change the balance
    MarenAccount.show_balance()

