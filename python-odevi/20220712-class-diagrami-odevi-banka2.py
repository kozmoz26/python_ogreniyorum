
class Bank:
    def __init__(self,bankid:int,name:str,location:str):
        self.bankid=bankid
        self.name=name
        self.location=location

class Teller:
    def __init__(self,id:int,name:str):
        self.id=id
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
    def __init__(self,id:int,name:str,address:str,phoneNo:int,acctNo:int):
        self.id=id
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
    def __init__(self,id:int,type:str,accountid:int,customerid:int):
        self.id=id
        self.type=type
        self.accountid=accountid
        self.customerid=customerid      

        
class Account:
    def __init__(self,id:int,customerid:int):
        self.id=id
        self.customerid=customerid

class Checking(Account):
    def __init__(self, id: int, customerid: int):
        super().__init__(id, customerid)

class Savings(Account):
    def __init__(self, id: int, customerid: int):
        super().__init__(id, customerid)



        






















