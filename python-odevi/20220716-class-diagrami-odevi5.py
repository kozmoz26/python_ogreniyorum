

class Maneger:
    def __init__(self,name:str,id:int,phoneNo:int,location:str):
        self.name=name
        self.id=id
        self.phoneNo=phoneNo
        self.location=location
    
    def PurchaseInventory(self):
        pass
    def RecordComplaints(self):
        pass
    def ManageStaff(self):
        pass

class Inventory:
    def __init__(self,type:str,status:str):
        self.type=type
        self.status=status

class Guest:
    def __init__(self,name:str,id:int,phoneNo:int,address:str,roomNo:int):
        self.name=name
        self.id=id
        self.phoneNo=phoneNo
        self.address=address
        self.roomNo=roomNo
    
    def Check_İn(Self):
        pass
    def Check_Out(self):
        pass
    def PayBill(self):
        pass
    def OrderFood(self):
        pass
    def SubmitFeedback(self):
        pass

class Chef:
    def __init__(self,name:str,id:int,location:str):
        self.name=name
        self.id=id
        self.location=location
        
    def TakeOrders(self):
        pass  

class FoodItems:
    def __init__(self,id:int,name:str):
        self.id=id
        self.name=name
        
class Housekeeping:
    def __init__(self,name:str,id:int,location:str):
        self.name=name
        self.id=id
        self.location=location
    
    def CleanRoom(self):
        pass

class Receptionist:
    def __init__(self,name:str,id:int,phoneNo:int,location:str):
        self.name=name
        self.id=id
        self.phoneNo=phoneNo
        self.location=location

    def CheckRoomAvailability(self):
        pass
    def BookRoom(self):
        pass
    def GenerateBill(self):
        pass
    def AcceptCustomerFeedback(self):
        pass

class Rooms:
    def __init__(self,roomNo:int,location:str):
        self.roomNo=roomNo
        self.location=location

class Bill:
    def __init__(self,billNo:int,guestName:int):
        self.billNo=billNo
        self.guestName=guestName
        

        












