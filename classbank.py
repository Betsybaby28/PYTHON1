class Bank:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def display(self):
        print("account no is %d,name is %s and balance is %d" % (self.account_number, self.name, self.balance))
    def deposit(self,deposit):
        self.balance=self.balance+deposit
    def withdrawl(self,withdrawl):
        self.balance=self.balance-withdrawl
    def bankfees(self,bankfees):
        self.balance=(5/100)*self.balance
betsy_account=Bank(227678374,"betsy",30000)
betsy_account.deposit(3000)
betsy_account.withdrawl(1000)
betsy_account.display()

