from datetime import datetime

class Amount:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount:.2f} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        transaction = Amount(amount, 'DEPOSIT')
        self.transactions.append(transaction)
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
            return
        transaction = Amount(amount, 'WITHDRAWAL')
        self.transactions.append(transaction)
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def print_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    def __add__(self, amount: float):
        self.deposit(amount)

    def __sub__(self, amount: float):
        self.withdraw(amount)

# Sample Test with User Inputs
if __name__ == "__main__":
    # Create an instance of PersonalAccount
    account = PersonalAccount(account_number=123456, account_holder="John Doe")

    # Demonstrate functionality
    print(account)

    # Deposit money
    account.deposit(100.0)
    
    # Withdraw money
    account.withdraw(50.0)
    
    # Check balance
    print(f"Current Balance: ${account.get_balance():.2f}")
    
    # Print transaction history
    account.print_transaction_history()