
class Bank:
    def __init__(self,bankid:int,name:str,location:str):
        self.bankid=bankid
        self.name=name
        self.location=location

class Teller:
    def __init__(self,ıd:int,name:str):
        self.ıd=ıd
        self.name=name

    def CollectMoney(self):
        pass
    def OpenAccount(self):
        pass
    def CloseAccount(self):
        pass
    def LoanRequest(self):
        pass
    def ProvideInfo(self):
        pass
    def IssueCard(self):
        pass

class Customer:
    def __init__(self,ıd:int,name:str,address:str,phoneNo:int,acctNo:int):
        self.ıd=ıd
        self.name=name
        self.address=address
        self.phoneNo=phoneNo
        self.acctNo=acctNo

    def GeneralInquiry(self):
        pass
    def DepositMoney(self):
        pass
    def WithdrawMoney(self):
        pass
    def OpenAccount(self):
        pass
    def CloseAccount(self):
        pass
    def ApplyForLoan(self):
        pass
    def RequestCard(self):
        pass

class Loan:
    def __init__(self,ıd:int,type:str,accountıd:int,customerıd:int):
        self.ıd=ıd
        self.type=type
        self.accountıd=accountıd
        self.customerıd=customerıd      

        
class Account:
    def __init__(self,ıd:int,customerıd:int):
        self.ıd=ıd
        self.customerıd=customerıd

class Checking(Account):
    def __init__(self, ıd: int, customerıd: int):
        super().__init__(ıd, customerıd)

class Savings(Account):
    def __init__(self, ıd: int, customerıd: int):
        super().__init__(ıd, customerıd)



        






















