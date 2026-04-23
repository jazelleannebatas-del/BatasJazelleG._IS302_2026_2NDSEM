class BankAccount_jab:
    def __init__(self_jab, balance_jab):
        self_jab.__balance = balance_jab

    def deposit_jab(self_jab, amount_jab):
        self_jab.__balance += amount_jab

    def withdraw_jab(self_jab, amount_jab):
        if amount_jab <= self_jab.__balance:
            self_jab.__balance -= amount_jab
        else:
            print("Insufficient funds")

    def get_balance_jab(self_jab):
        return self_jab.__balance

account_jab = BankAccount_jab(5000)
account_jab.deposit_jab(1000)
account_jab.withdraw_jab(2000)
print("Balance_jab:", account_jab.get_balance_jab())