class bankAccount():
    def __init__(self, account_holder="bank account", balance=100000):
        self.__account_holder=account_holder
        self.__balance=balance
    def withdraw(self,amount):
        self.__balance=self.__balance + amount
        print ("your new balance is", self.__balance)
    def deposit(self,amount):
        self.__balance=self._balance + amount
        print("your new balance is", self.__balance)


class fixed_account(bankAccount):
    def __init__(self,account_holder="fixed account", balance=1000000):
        self._account_holder=account_holder
        self.__balance=balance
        super .__init__()
    def withdraw(self,amount):
        if amount>20000:
            print"cannot process this request, contact your bank"
        else:
            self.__balance=self.__balance-amount
            print("your account now has:", self.__balance)

class savingsaccount(bankAccount):
    def __init__(self,account__holder="savingsaccount", balance=20000):
        self.__account_holder = account_holder
        self.__balance=balance
        super.__init__()
    def deposit(self,amount):
        self.__balance= self.__balance+(amount*1.10)
        print ("your account now has:", self.__balance)



