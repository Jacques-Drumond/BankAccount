class BankAccount:
    
    active_accounts = 0
    
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        BankAccount.active_accounts += 1
    
    def deposit(self, add_value):
        self.balance = self.balance + add_value
        return self.balance
    
    def withdraw(self, withdraw_value):
        self.balance = self.balance - withdraw_value
        return self.balance

name = input("What is your name?\n")

account1 = BankAccount(name)

answer = input("Type the option wanted: Balance .. Name .. Deposit .. Withdraw .. Quit\n")

while answer != "Quit":

    if answer == "Balance":
        print(account1.balance)
        answer = input("Type the option wanted: Balance .. Name .. Deposit .. Withdraw .. Quit\n")
    elif answer == "Name":
        print(account1.owner)
        answer = input("Type the option wanted: Balance .. Name .. Deposit .. Withdraw .. Quit\n")
    elif answer == "Deposit":
        value = int(input("How much do you want to depoist?"))
        account1.deposit(value)
        answer = input("Type the option wanted: Balance .. Name .. Deposit .. Withdraw .. Quit\n")
    elif answer == "Withdraw":
        with_value = int(input("How much do you want to withdraw?"))
        if account1.balance < with_value:
            print("You can't withdraw that value")
            answer = input("Type the option wanted: Balance .. Name .. Deposit .. Withdraw .. Quit\n")
        else:
            account1.withdraw(with_value)
            answer = input("Type the option wanted: Balance .. Name .. Deposit .. Withdraw .. Quit\n")



