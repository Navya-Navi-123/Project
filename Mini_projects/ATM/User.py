class user:
    def __init__(self):
        self.card=20000
    def choose(self):
        while True:
            print("please choose your card type \n1. Rupay\n2. Visa\n3. Master\n")
            self.a=input()
            self.a=self.a.lower()
            if self.a=="rupay" or self.a=="1":
                self.a="rupay"
                print("Please insert your RUPAY card")
                break
            elif self.a=="visa" or self.a=="2":
                self.a="visa"
                print("Please insert your VISA card")
                break
            elif self.a=="master" or self.a=="3":
                self.a="master"
                print("Please insert your MASTER card")
                break
            else:
                print("ATM will not accept you card")
    def login(self):
        while True:
            self.user=input("Enter the User Name:")
            self.user=self.user.lower()
            self.password=input("Enter the Password:")
            self.password=self.password.lower()
            if self.user==self.password:
                pass
                break
            else:
                print("Please enter the correct details")
    def check(self):
        print("The balance in the account is",self.card)
    def with_drawl(self):
        while True:
            if self.a=="rupay":
                print("the Limit for the Rupay card is 2000.")
                amt=int(input("Enter the amount you want to withdrawl:"))
                if amt>2000:
                    print("limit has crossed.Please enter lesser amount \n Try again")
                elif amt<=2000:
                    if amt<(self.card):    
                        self.card=self.card-amt
                        print("The amount you have withdrawn from the account is ",amt,".")
                        print("The balance in the account is",self.card)
                        break
                    else:
                        print("you dont have sufficeint balance")
            elif self.a=="visa":
                print("The limit for the Visa card is 5000.")
                amt=int(input("Enter the amount you want to withdrawl:"))
                if amt>5000:
                    print("limit has crossed.Please enter lesser amount \n Try again")
                elif amt<=5000:
                    if amt<(self.card):    
                        self.card=self.card-amt
                        print("The amount you have withdrawn from the account is ",amt,".")
                        print("The balance in the account is",self.card)
                        break
                    else:
                        print("you dont have sufficeint balance")
            elif self.a=="master":
                print("The limit for the Master card is 8499.")
                amt=int(input("Enter the amount you want to withdrawl:"))
                if amt>8499:
                    print("limit has crossed.Please enter lesser amount \n Try again")
                elif amt<=8499:
                    if amt<(self.card):    
                        self.card=self.card-amt
                        print("The amount you have withdrawn from the account is ",amt,".")
                        print("The balance in the account is",self.card)
                        break
                    else:
                        print("you dont have sufficeint balance")
            else:
                pass
    def cash_deposit(self):
        amt=int(input("Enter the amount you want to credit"))
        print("The amount you have deposited in the account is",amt,".")
        self.card=self.card+amt
        print("The balance in the account is",self.card)
    def mini(self,option):
        print("1. The transaction that was done before is checking the balance\nThe balance that was in the account is 20000")
        print("2. The last transaction was failed")
        print("3. The transaction done was the option specified is",option,"\n Now the balance in your account was",self.card)   
obj=user()
obj.choose()
obj.login()
while True:
    option=input("Which of the following options you want to choose:\n1.Check Balance\n2.Cash Withdrawl\n3.Cash Deposit\n4.Mini Statement\n")
    option=option.lower()
    if option=="check balance"or option=="1":
        option="check balance"
        obj.check()
        
    elif option=="cash withdrawl" or option=="2":
        option="cash withdrawl"
        obj.with_drawl()
        
    elif option=="cash deposit" or option=="3":
        option="cash deposit"
        obj.cash_deposit()
        
    elif option=="mini statement" or option=="4":
        option="mini statement"
        obj.mini(option)
        
    else:
        print("Exited from the atm")
        break