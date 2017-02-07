class  BankAccount():
    def __init__(self, type, amount):
        self.type = type
        self.balance = amount
        self.overdraft_fees = 0
        print("New {} account made with starting balance ${}.".format(self.type, self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("${} deposit made. New balance ${}.".format(amount, self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        print("${} withdrawn. New balance ${}.".format(amount, self.balance))
        if self.balance < 0:
            self.overdraft_fees +=20
            print("$20 overdraft fee incurred.  Total fees of ${}".format(self.overdraft_fees))

    def check_balance(self, amount):
        print("Balance: ", self.balance)


tommy_account = BankAccount("checking", 1000)
tommy_account.check_balance
tommy_account.deposit(500)
tommy_account.withdraw(300)
tommy_account.withdraw(1300)
