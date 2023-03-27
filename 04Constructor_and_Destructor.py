# การสร้าง Class และ Object
# Class
class Employee:
    # Method
    def detail(self,name,salary,department):
        # print("เรียกใช้งาน Method ใน Class Employee")
        # กำหนดคุณสมบัติ
        self.name = name
        self.salary = salary
        self.department = department

    def showdata(self):
        print(f'ชื่อพนักงาน : {self.name}')
        print(f'เงินเดือน : {self.salary}')
        print(f'ตำแหน่งงาน : {self.department}')


# Object เรียกใช้งาน Class
obj1 = Employee()
obj1.detail("สมชาย",200,"Programmer")

obj2 = Employee()
obj2.detail("สมหญิง",1000,"Photographyer")

obj3 = Employee()
obj3.detail("จิตรดี",2000,"Made")

obj1.showdata()
obj2.showdata()
obj3.showdata()