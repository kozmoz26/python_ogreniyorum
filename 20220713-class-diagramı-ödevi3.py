

# class Customer:
#     def __init__(self,ıd:int,name:str,address:str,phone:str):
#         self.ıd=ıd
#         self.name=name
#         self.address=address
#         self.phone=phone
    
#     def Add(self):
#         pass
#     def Edir(self):
#         pass
#     def Delete(self):
#         pass

# class Order:
        

class Student:

    def __init__(self, id):
        self.id = id

    def registration_number(self, department_id):
        return str(self.id) + '-' + department_id


class Department:

    def __init__(self, id, student):
        self.id = id
        self.student = student

    def student_registration(self):
        return self.student.registration_number(self.id)


if __name__ == '__main__':
    student = Student(10)
    department = Department('ENG', student)
    print(department.student_registration())






