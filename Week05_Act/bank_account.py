class BankAccount_jab:
    def __init__(self_jab, account_name_jab, balance_jab):
        self_jab.account_name_jab = account_name_jab
        self_jab.balance_jab = balance_jab
    
    def deposit_jab(self_jab, amount_jab):
        self_jab.balance_jab += amount_jab
        print("Deposit successful")
    
    def withdraw_jab(self_jab, amount_jab):
        if amount_jab <= self_jab.balance_jab:
            self_jab.balance_jab -= amount_jab
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_jab(self_jab):
        print("Balance:", self_jab.balance_jab)

account_jab = BankAccount_jab("Juan", 5000)
account_jab.deposit_jab(1000)
account_jab.withdraw_jab(2000)
account_jab.display_balance_jab()
