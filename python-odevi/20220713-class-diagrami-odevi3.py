

from datetime import datetime


class Customer:
    def __init__(self,id:int,name:str,address:str,phone:str):
        self.id=id
        self.name=name
        self.address=address
        self.phone=phone
    
    def Add(self):
        pass
    def Edir(self):
        pass
    def Delete(self):
        pass

class Order:
    def __init__(self,id:int,customerID:int,customerName:str,productID:int,amount:int,date:datetime):
        self.id=id
        self.customerID=customerID
        self.customerName=customerName
        self.productID=productID
        self.amount=amount
        self.date=date
    
    def NewOrder(self):
        pass
    def Edit(self):
        pass

class Product:
    def __init__(self,id:int,price:float,type:str):
        self.id=id
        self.price=price
        self.type=type

    def Add(self):
        pass
    def Modify(id:int):
        pass
    def select(id:int):
        pass


class Stock:
    def __init__(self,productID:int,quality:str,no:int):
        self.productID=productID
        self.quality=quality
        self.no=no

    def Add(self):
        pass
    def Modify(productID:int):
        pass
    def select(productID:int):
        pass

        




        
        
        










