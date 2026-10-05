class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"deposit:{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transaction_history.append(f"withdraw:{amount}")
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, other_account, amount):
        if not self.withdraw(amount):
            return
        other_account.deposit(amount)
