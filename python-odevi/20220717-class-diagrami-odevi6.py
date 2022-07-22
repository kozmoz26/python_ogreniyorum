
import random

class Informations:
    def __init__(self,name:str,address:str,id:int):
        self.name=name
        self.address=address
        self.id=id

    def GetAddress(self):
        self.address=input("adresinizi girin")
        return self.address

    def Getname(self):
        self.name=input("isminizi girin")
        return self.name

    def Getid(self):
        return id(self.id)

class Employee(Informations):
    def __init__(self, name: str, address: str, id: int,phoneNo:int, isManager:bool):
        super().__init__(name, address, id)

    def beManager(employe):
       employe.isManager = True
       return "İşlem başarılı"


class Company(Informations):
    def __init__(self, name: str, address: str, id: int):
        super().__init__(name, address, id)

class Office(Informations):
    def __init__(self, name: str, address: str, id: int):
        super().__init__(name, address, id)

class Headquarter(Informations):
    def __init__(self, name: str, address: str, id: int):
        super().__init__(name, address, id)

class Department(Informations):
    def __init__(self, name: str, address: str, id: int,managedby:str):
        super().__init__(name, address, id,managedby)
    
    def GetManager(self):
        if Employee.BeManager==True:
            return True
        else
            return False





        







        
















