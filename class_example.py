class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -=amount
        print("rs-",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance +=amount
        print("rs-",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance

    
acc1=account(10000,12345560)
print( "your balance=",acc1.balance)
acc1.debit(5000)
acc1.credit(1200)