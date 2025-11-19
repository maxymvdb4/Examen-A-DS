from BankAccount import BankAccount

accounts_list = [BankAccount("NL1", 1000.00), BankAccount("NL2", 500.00), BankAccount("NL3", 1200.50)]

def accountcheck(account: str, accountlist: list):
    for i in accountlist:
        if i.account_number == account:
            return True
    return False


def transfer_funds(source_account: str, target_account: str, amount: float, accounts__list: list):
    assert accountcheck(source_account, accounts__list), "Source account does not exist"
    assert accountcheck(target_account, accounts__list), "Target account does not exist"
    assert amount > 0, "Amount must be greater than zero"
    for i in accounts__list:
        if i.account_number == source_account:
            x1 = i
    for j in accounts__list:
        if j.account_number == target_account:
            x2 = j
    if x1.daily_limit + amount > 1000:
        return "This amount puts you over the daily limit"
    elif x1.withdraw(amount):
        x2.deposit(amount)
        return "Overboeking geslaagd"
    elif x1.balance < amount:
        return "Balance insufficient"




def new_day(accouts__list: list):
    for i in accouts__list:
        BankAccount.reset_daily_limit(i)

transfer_funds("NL1", "NL2", 10.00, accounts_list)
transfer_funds("NL1", "NL5", 100.00, accounts_list)
transfer_funds("NL3", "NL1", 1001.00, accounts_list)
new_day(accounts_list)








