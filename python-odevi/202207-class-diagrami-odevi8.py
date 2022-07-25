
class Customer:
    def __init__(self,name):
        self.name=name

    def GetName(self):
        self.name=input("ders ismi nedir")
        return self.name 

class Order:
    def __init__(self,details,products):
        self.details=details
        self.products=products

class PaymentMethod:
    def __init__(self,cash,creditCard,check) -> None:
        self.cash=cash
        self.creditCard=creditCard
        self.check=check






