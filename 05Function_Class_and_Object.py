# การสร้าง Class และ Object
# Class
class Employee:
    # Method

    # Constructor
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showdata(self):
        print(f'ชื่อพนักงาน : {self.name}')
        print(f'เงินเดือน : {self.salary}')
        print(f'ตำแหน่งงาน : {self.department}')

    # Destructor
    def __del__(self):
        print("Call Destructor")

# Object เรียกใช้งาน Class
obj1 = Employee("สมชาย",200,"Programmer")
obj2 = Employee("สมหญิง",1000,"Photographyer")
obj3 = Employee("จิตรดี",2000,"Made")


print(isinstance(obj1,Employee)) # obj1 เรียกใช้ Class Employee รึเปล่า
print(dir(obj1)) # แสดง Method ทั้งหมดภายใน Class
print(obj1.__class__) #เรียกว่ามาจาก Class ใด