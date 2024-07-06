 #toyota,mahindra,mercedes
#first function
#take the input from the user for the car company name and in the input message give the user the option of three companies
#and the user input company name goes as the input/arguments to model name function,which welcomes the user accordingly to the company name.
#ask the user to enter the specific model name for that company
#second function
#whose name is variant. according to the car company name and car model the user should be asked to enter the variant he would like to choose from
#petrol,desiel
#third function display function
#according to the car company and car model name and car variant first its ex showroom price should be displayed and
#then its on road price should be displayed,which is calculated as ex showroom price+cgst+sgst+insurance.
#the sgst,cgst and the insurance all the three have a common value throughout the car show room
#sgst,cgst and the insurance should be in percentages.
class showroom:
    def __init__(self):
        print("welcome")
        while True:
            print("In our showroom we had different companies like \n1.TOYOTA\n2.MAHINDRA\n3.MERCEDES")
            self.com_name=input("Please choose the company which you want to buy:")
            self.com_name=self.com_name.lower()
            if self.com_name=="toyota" or self.com_name=="mahindra" or self.com_name=="mercedes" or self.com_name=="1" or self.com_name=="2" or self.com_name=="3":
                if self.com_name=="toyota" or self.com_name=="1":
                    print("Welcome to the Toyota Family")
                    break
                elif self.com_name=="mercedes" or self.com_name=="3":
                    print("Welcome to the Mercedes Family")
                    break
                elif self.com_name=="mahindra" or self.com_name=="2":
                    print("Welcome to the Mahindra Family")
                    break
            else:
                print("we dont have that company name cars.")
        self.cgst=(18/10)
        self.sgst=(18/100)
        self.insurance=(18/100)
    def choose(self):
        if self.com_name=="toyota"or self.com_name=="1":
            while True:
                print("we have different models in the toyota like 1.HILUX\n2.CAMRY")
                m_toyota=input("please choose from the models we have:")
                m_toyota=m_toyota.lower()
                if m_toyota=="hilux" or m_toyota=="camry" or m_toyota=="1" or m_toyota=="2":
                    print("ok\n please let us know in which variant you prefer :1.petrol\n2.diesel")
                    var_name=input()
                    var_name=var_name.lower()
                    if var_name=="petrol"or var_name=="1":
                        if m_toyota=="hilux"or m_toyota=="1":
                            ex_showroom_price=25000
                            print("the Ex show room price of the company toyota and the model hilux the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        elif m_toyota=="camry" or m_toyota=="2":
                            ex_showroom_price=35000
                            print("the Ex show room price of the company toyota and the model camry the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        else:
                            print("we dont have that type of cars")
                    elif var_name=="diesel" or var_name=="2":
                        if m_toyota=="hilux"or m_toyota=="1":
                            ex_showroom_price=27000
                            print("the Ex show room price of the company toyota and the model hilux the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        elif m_toyota=="camry" or m_toyota=="2":
                            ex_showroom_price=37000
                            print("the Ex show room price of the company toyota and the model camry the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        else:
                            print("we dont have that type of cars")
                    else:
                        print("we dont have that variant")
        elif self.com_name=="mahindra"or self.com_name=="2":
            while True:
                print("we have different models in the mahindra like 1. THAR \n2. SCORPIO")
                m_mahindra=input("please choose from the models we have:")
                m_mahindra=m_mahindra.lower()
                if m_mahindra=="thar"  or m_mahindra=="scorpio" or m_mahindra=="1" or m_mahindra=="2":
                    print("ok \nplease let us know in which variant you prefer :1.petrol \n2. diesel")
                    var_name=input()
                    var_name=var_name.lower()
                    if var_name=="petrol"or var_name=="1":
                        if m_mahindra=="thar"or m_mahindra=="1":
                            ex_showroom_price=28000
                            print("the Ex show room price of the company mahindra and the model thar the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        elif m_mahindra=="scorpio" or m_mahindra=="2":
                            ex_showroom_price=38000
                            print("the Ex show room price of the company mahindra and the model scorpio the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        else:
                            print("we dont have that type of cars")
                    elif var_name=="diesel"or var_name=="2":
                        if m_mahindra=="thar"or m_mahindra=="1":
                            ex_showroom_price=30000
                            print("the Ex show room price of the company mahindra and the model thar the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        elif m_mahindra=="scorpio" or m_mahindra=="2":
                            ex_showroom_price=39000
                            print("the Ex show room price of the company mahindra and the model scorpio the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        else:
                            print("we dont have that type of cars")
                    else:
                        print("we dont have that variant")
        elif self.com_name=="mercedes" or self.com_name=="3":
            while True:
                print("we have different models in the mercedes like 1. EQB \n 2. GLB")
                m_mercedes=input("please choose from the models we have:")
                m_mercedes=m_mercedes.lower()
                if m_mercedes=="1" or m_mercedes=="2" or m_mercedes=="eqb" or m_mercedes=="glb":
                    print("ok")
                    print("please let us know in which variant you prefer :1. petrol \n 2. diesel")
                    var_name=input()
                    var_name=var_name.lower()
                    if var_name=="petrol"or var_name=="1":
                        if m_mercedes=="eqb" or m_mercedes=="1":
                            ex_showroom_price=45000
                            print("the Ex show room price of the company mercedes and the model EQB the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        elif m_mercedes=="glb"or m_mercedes=="2":
                            ex_showroom_price=55000
                            print("the Ex show room price of the company mercedes and the model GLB the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        else:
                            print("we dont have that type of cars")
                    elif var_name=="diesel" or var_name=="2":
                        if m_mercedes=="eqb" or m_mercedes=="1":
                            ex_showroom_price=47000
                            print("the Ex show room price of the company mercedes and the model EQB the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        elif m_mercedes=="glb"or m_mercedes=="2":
                            ex_showroom_price=57000
                            print("the Ex show room price of the company mercedes and the model GLB the Ex show room price is ",ex_showroom_price)
                            our_price=ex_showroom_price+(self.cgst*ex_showroom_price)+ (self.sgst*ex_showroom_price)+(self.insurance*ex_showroom_price)
                            print("our price for your selection is ",our_price)
                            break
                        else:
                            print("we dont have that type of cars")
                    else:
                        print("we dont have that variant")
        else:
            print("we dont have that model")
        
sr=showroom()
sr.choose()

