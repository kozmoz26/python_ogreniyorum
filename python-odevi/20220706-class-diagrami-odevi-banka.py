
class Customer:
    def __init__(self,name,addres,dob,card_number,pin):
        self.name=name
        self.addres=addres
        self.dob=dob
        self.card_number=card_number
        self.pin=pin

    def verifyPassword(self,pin):
        if (self.pin==pin):
            return True
        else :
            return False
        

class ATM:
    def __init__(self,location,managedby):
        self.location=location
        self:managedby=managedby
    
    def identifies(self):
        pass
    def transections(self):
        pass


class Bank:
    def __init__(self,code,address):
        self.code=code
        self.address=address

    def manages(self):
        pass
    def maintains(self):
        pass


class ATMTransaction:
    def __init__(self,transactionId,date,type,amount,postBalance):
        self.transactionId=transactionId
        self.date=date
        self.type=type
        self.amount=amount
        self.postBalance=postBalance

    def modifies(self):
        pass


class Account:
    def __init__(self,number,balance):
        self.number=number
        self.balance=balance

    def deposit(self):
        pass
    def withdraw(self):
        pass
    def createTransaction(self):
        pass


class CurrentAccount(Account):
    def __init__(self, number, balance,accountNo):
        super().__init__(number, balance,accountNo)

    def withdraw(self):
        return super().withdraw()
    

class SavingAccount(Account):
    def __init__(self, number, balance,accountNo):
        super().__init__(number, balance,accountNo)




        

    












