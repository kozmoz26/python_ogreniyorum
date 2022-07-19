

from inspect import _void
from xmlrpc.client import boolean


class Bank:
    def __init__(self,code:int,location:str):
        self.code=code
        self.location=location
    
    def Manages(self):
        pass
    def Security(self):
        pass

class Customer:
    def __init__(self,name:str,address:str,idno:int,cardnumber:int,password):
        self.name=name
        self.address=address
        self.idno=idno
        self.cardnumber=cardnumber
        self.password=password

    def login(Self)->boolean:
        pass    

class ATM:
    def __init__(self,location:str,money:int):
        self.location=location
        self.money=money

    def Auth(self)->bool:
        pass
    def Transaction(self)->_void:
        pass

class ATMTransaction:
    def __init__(self,location:str,money:int):
        self.location=location
        self.money=money

    def Auth(self)->bool:
        pass
    def Transaction(self)->_void:
        pass

class Account:
    def __init__(self,number:int,balance:int):
        self.number=number
        self.balance=balance

    def Deposit(amount:int)->boolean:
        pass
    def Withdraw(amount:int)->boolean:
        pass
    def Transaction(self)->_void:
        pass

class MainAccount(Account):
    def __init__(self, number: int, balance: int):
        super().__init__(number, balance)

    def Transaction(self) -> _void:
        return super().Transaction()

class SavingAccount(Account):
    def __init__(self, number: int, balance: int):
        super().__init__(number, balance)

    def Transaction(self) -> _void:
        return super().Transaction()


        












