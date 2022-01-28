class Bank:
    def __init__(self):
        self.Client_detail_list=[]
        self.Loggedin=False
        self.Cash=100
        self.Transfercash=False

    def Register(self, Name, PhoneNo, Password):
        Cash=self.Cash
        Condition=True
        if len(str(PhoneNo))>10 or len(str(PhoneNo))<10:
            print("Invalid Phone Number")
            Condition=False
        if len(Password)<5 or len(Password)>18:
            print("Enter Password Greater Than 5 and Less Than 18")
            Condition=False
        if Condition==True:
            print("Account Created Successfully")
            self.Client_detail_list=[Name, PhoneNo, Password, Cash]
            with open (f"{Name}.txt","w") as p:
                for detail in self.Client_detail_list:
                    p.write(str(detail)+"\n")
    
    def Login(self, Name, PhoneNo, Password):
        with open(f"{Name}.txt","r") as p:
            detail=p.read()
            self.Client_detail_list=detail.split("\n")
            if str(PhoneNo) in str(self.Client_detail_list):
                if str(Password) in str(self.Client_detail_list):
                    self.Loggedin=True
            if self.Loggedin==True:
                print(f"{Name} logged in")
                self.Cash=int(self.Client_detail_list[3])
                self.Name=Name
            else:
                print("wrong details")

    def Add_Cash(self,Amount):
        if Amount>0:
            self.Cash+=Amount
            with open(f"{Name}.txt","r") as p:
                detail=p.read()
                self.Client_detail_list=detail.split("\n")
            with open(f"{Name}.txt","w") as p:
                p.write(detail.replace(self.Client_detail_list[3],str(self.Cash)))
                print("Amount Add Successfully")
        else:
            print("Correct Amount Fill")

    def Cash_Transfer(self, Name, Amount, PhoneNo):
        with open(f"{Name}.txt","r") as p:
            detail=p.read()
            self.Client_detail_list=detail.split("\n")
            if str(PhoneNo) in self.Client_detail_list:
                self.Transfercash=True

        if self.Transfercash== True:
            total_cash=int(self.Client_detail_list[3])+Amount
            left_cash=self.Cash-Amount
            with open(f"{Name}.txt","w") as p:
                p.write(detail.replace(str(self.Client_detail_list[3]),str(total_cash)))

            with open(f"{Name}.txt","r") as p:
                detail_2=p.read()
                self.Client_detail_list= detail_2.split("\n")
            
            with open(f"{Name}.txt","w") as p:
                p.write(detail.replace(str(self.Client_detail_list[3]),str(left_cash)))
            print("Amount Transfer to Successfully to",Name, PhoneNo)
            print("Balace_left=",left_cash)
            self.Cash=left_cash

    def Password_Change(self, Password):
        if len(Password)<5 or len(Password)>18:
            print("Enter Password Greater Than 5 and Less Than 18")
        else:
            with open(f"{Name}.txt","r") as p:
                detail=p.read()
                self.Client_detail_list=detail.split("\n")

            with open(f"{Name}.txt","w") as p:
                p.write(detail.replace(str(self.Client_detail_list[2]),str(Password)))
            print("new passowrd set up successfully")

    def Phone_change(self,PhoneNo):
        if len(str(PhoneNo))>10 or len(str(PhoneNo))<10:
            print("Invalid Phone Number Please Enter Correct Phone Number")
        else:
            with open(f"{Name}.txt","r") as p:
                detail=p.read()
                self.Client_detail_list=detail.split("\n")

            with open(f"{Name}.txt","w") as p:
                p.write(detail.replace(str(self.Client_detail_list[1]),str(PhoneNo)))        
            print("Phone Number Change Successfully")            
if __name__=="__main__":
    Bank_object=Bank()
    print("Welcome to my Krishna Bank")
    print("1.Login")
    print("2.Creata a new Account")
    user = int(input("Input Here: "))

    if user ==1:
        print("logging in")
        Name=input("Enter Name:")
        PhoneNo=input("Enter Phone Number:")
        Password=input("Enter Password:")
        Bank_object.Login(Name, PhoneNo, Password)
        while True:
            if Bank_object.Loggedin:
                print("1. Add Amount")
                print("2. Check Balance")
                print("3. Transfer Amount")
                print("4. Edit Profile")
                print("5. Logout")
                login_user = int(input())                
                if login_user==1:
                    print("Balance=",Bank_object.Cash)
                    Amount=int(input("Enter Amount:"))
                    Bank_object.Add_Cash(Amount)
                    print("\n1.Back Menu")
                    print("2. Logout")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        break
                elif login_user==2:
                    print("Balance=",Bank_object.Cash)
                    print("\n1. Back Menu")
                    print("2. Logout")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        break
                elif login_user==3:
                    print("Balance=",Bank_object.Cash)
                    Amount=int(input("Enter a Amount:"))
                    if Amount>0 and Amount<=Bank_object.Cash:
                        Name=input("Enter Person Name:")
                        PhoneNo=input("Enter Person Phone Number:")
                        Bank_object.Cash_Transfer(Name, Amount, PhoneNo)
                        print("\n1. Back Menu")
                        print("2. Logout")
                        choose=int(input())
                        if choose==1:
                            continue
                        if choose==2:
                            break
                    elif Amount<0:
                        print("Enter please correct value of amount")
                    elif Amount>Bank_object.Cash:
                        print("Not enough Balance")
                elif login_user==4:
                    print("1. Password change")
                    print("2. Phone Number change")
                    Edit_Profile=int(input())
                    if Edit_Profile==1:
                        Password=input("Enter New Password")
                        Bank_object.Password_Change(Password)
                        print("\n1. Back Menu")
                        print("2. Logout")
                        choose=int(input())
                        if choose==1:
                            continue
                        if choose==2:
                            break
                    elif Edit_Profile==2:
                        PhoneNo=int(input("Enter New Phone Number"))
                        Bank_object.Phone_change(PhoneNo)
                        print("\n1. Back Menu")
                        print("2. Logout")
                        choose=int(input())
                        if choose==1:
                            continue
                        if choose==2:
                            break

                elif login_user==5:
                    break
    if user==2:
        print("Creating a New Account")
        Name=input("Enter Name:")
        PhoneNo=int(input("Enter Phone Number:"))
        Password=input("Enter Password:")
        Bank_object.Register(Name, PhoneNo, Password)
