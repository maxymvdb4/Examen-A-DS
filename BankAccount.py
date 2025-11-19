class BankAccount:
    def __init__(self, account_number: str, balance: float, daily_limit: float = 0.0):
        assert account_number[0:2] == "NL" or account_number[0:2] == "BE", "Account number must be NL or BE"
        self.account_number = account_number
        self.balance = balance
        self.daily_limit = daily_limit
        self.amount_withdrawn_today = 0.0

    def deposit(self, amount: float):
        assert amount > 0.0, "Amount must be greater than zero"
        assert 1000 > self.daily_limit + amount, "This amount puts you over the daily limit"
        self.balance += amount
        self.daily_limit += amount

    def withdraw(self, amount: float):
        if amount < 0.0:
            print("Amount must be greater than zero")
            return False
        elif self.daily_limit + amount > 1000.0:
            print("This amount puts you over the daily limit")
            return False
        elif self.balance < amount:
            print("Balance insufficient")
            return False
        else:
            self.balance -= amount
            self.amount_withdrawn_today += amount
            self.daily_limit += amount
            return True

    def reset_daily_limit(self):
        self.daily_limit = 0.0

    def __str__(self):
        return f"Accountnumber: {self.account_number}, Balance: {self.balance:.2f}, Daily limit: {self.daily_limit:.2f}"

















