# initializes a class(bankAccount) with variables
class bankAccount():

    def __init__(self, account_holder="bank account", balance=100000):
        self.__account_holder=account_holder
        self.__balance=balance
        # a function to allow a user to withdraw some amount from his/her account and view the balance
    def withdraw(self,amount):
        self.__balance=self.__balance - amount
        print ("your new balance is", self.__balance)
        # displays the fuction to allow a user deposit some amount and give the balance in the account
    def deposit(self,amount):
        self.__balance=self._balance + amount
        print("your new balance is", self.__balance)

# a new class fixed_account , inheriting variables from class bankAccount

class fixed_account(bankAccount):
    def __init__(self,account_holder="fixed account", balance=1000000):
        self._account_holder=account_holder
        self.__balance=balance
        super .__init__()
        # a function to limit the amount withdrawn at an instance to 20000
    def withdraw(self,amount):
        if amount>20000:
            print"cannot process this request, contact your bank"
        else:
            self.__balance=self.__balance-amount
            print("your account now has:", self.__balance)
# a new class (savingsaccount) still inheriting variables from bankAccount
class savingsaccount(bankAccount):
    def __init__(self,account__holder="savingsaccount", balance=20000):
        self.__account_holder = account_holder
        self.__balance=balance

        # function  to calculate an intrest in amount and give back the cumulative balance
    def deposit(self,amount):
        self.__balance= self.__balance+(amount*1.10)
        print ("your account now has:", self.__balance)



