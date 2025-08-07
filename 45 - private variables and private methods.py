class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self.__balance = balance                # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} into account {self.__account_number}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from account {self.__account_number}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    # private method
    def __deduct_fees(self, fee):
        self.__balance -= fee

# Creating an instance of BankAccount
account1 = BankAccount("123456", 1000)

# Accessing public methods
print("Current balance:", account1.get_balance())
account1.deposit(500)
print("Current balance after deposit:", account1.get_balance())
account1.withdraw(200)
print("Current balance after withdrawl:", account1.get_balance())

# Trying to access private variables directly (will throw an error)
# print(account1.__balance)  # This will give an AttributeError

# Trying to access private method directly (will throw an error)
# account1.__deduct_fees(50)  # This will give an AttributeError
