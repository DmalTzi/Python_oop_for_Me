# การสร้าง Class และ Object
# Class
class Employee:
    # Method
    def detail(fles):
        # print("เรียกใช้งาน Method ใน Class Employee")
        # กำหนดคุณสมบัติ
        fles.name = "Dmalt"
        fles.salary = 50000
        print(f'ชื่อพนักงาน : {fles.name}')
        print(f'เงินเดือน : {fles.salary}')


# Object เรียกใช้งาน Class
emp1 = Employee()

emp1.detail()