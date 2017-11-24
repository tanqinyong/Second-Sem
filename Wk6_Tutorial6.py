class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def withdraw(self,amount):
        self.__balance -= amount

    def deposit(self,amount):
        self.__balance += amount


# def make_account():
#    return {'balance':0}
#
#
# def deposit(account, amount):
#    account['balance'] += amount
#    return account['balance']
#
#
# def withdraw(account, amount):
#    account['balance'] -= amount
#    return account['balance']
#
#
# a = make_account()
# b = make_account()
#
# print('Account a:', deposit(a, 100))
# print('Account b:', deposit(b, 500))
# print('Account a:', withdraw(a, 50))
# print('Account b:', withdraw(b, 50))
