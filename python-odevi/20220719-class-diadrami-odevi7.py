


from calendar import c


class Place:
    def __init__(self,name:str,id:int,address:str):
        self.name=name
        self.id=id
        self.address=address

    def GetAddress(self):
        self.address=input("adresinizi girin")
        return self.address
    def Getname(self):
        self.name=input("isminizi girin")
        return self.name

class Person:
    def __init__(self,name:str,phoneNo:int,address:str):
        self.name=name
        self.address=address
        self.phoneNo=phoneNo

    def GetName(self):
        self.name=input("isminizi girin")
        return self.name
    def GetPhoneNo(self):
        self.phoneNo=input("numaranızı girin")
        return self.phoneNo
    def Address(self):
        self.address=input("adresinizi girin")
        return self.address

class Subject:
    def __init__(self,name:str,topics:str):
        self.name=name
        self.topics=topics
        
    def Getname(self):
        self.name=input("ders ismi nedir")
        return self.name

class School(Place):
    def __init__(self, name: str, id: int, address: str):
        super().__init__(name, id, address)

    def GetAddress(self):
        return super().GetAddress()

    def Getname(self):
        return super().Getname()

class Department(Place):
    def __init__(self, name: str, id: int, address: str):
        super().__init__(name, id, address)

    def GetAddress(self):
        return super().GetAddress()

    def Getname(self):
        return super().Getname()

class Student(Person):
    def __init__(self, name: str, phoneNo: int, address: str):
        super().__init__(name, phoneNo, address)

    def GetName(self):
        return super().GetName()

    def GetPhoneNo(self):
        return super().GetPhoneNo()

class Instructor(Person):
    def __init__(self, name: str, phoneNo: int, address: str):
        super().__init__(name, phoneNo, address)

    def GetName(self):
        return super().GetName()

    def GetPhoneNo(self):
        return super().GetPhoneNo()













