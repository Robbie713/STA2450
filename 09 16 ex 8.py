class BankAccount:
"""
Doc Screen
"""
    def ser_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("error: balance cannot be negative")

    def get_balance(self):
        return self.__balance

    def withdraw(selfself, amount):
        if amount > self.__balance:
            print("insufficient funds")
        elif amount
