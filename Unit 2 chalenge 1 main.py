class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        return self.__account_balance


# Testing the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)

# Deposit money
account.deposit(500)

# Display account balance
print(f"Current balance: {account.display_balance()}")

# Withdraw money
account.withdraw(200)

# Display updated balance
print(f"Updated balance: {account.display_balance()}")