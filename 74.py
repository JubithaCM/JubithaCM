class bank:
    def __init__(self):
        self.bal=0
    def deposit(self):
        self.name=input("Enter Account holder's name")
        self.accnttype=input("Enter Account type")
        self.amount=int(input("Enter Amount to deposit"))
        self.bal=self.bal+self.amount
        print("Rs",self.amount,"Deposited Sucessfully")
    def withdrawal(self):
        self.wamount=int(input("Enter amount to withdraw"))
        if self.bal<self.wamount:
            print("INSUFFICIENT BALANCE")
        self.bal=self.bal-self.wamount
        print("Balance is RS",self.bal)
b=bank()
b.deposit()
b.withdrawal()
