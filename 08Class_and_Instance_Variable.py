# การสร้าง Class และ Object
# Class
class Employee:
    # Method

    # Class variable
    _minSalary = 12000
    _maxSalary = 50000

    # Constructor
    def __init__(self,name,salary,department):
        # Instace Variable
        self.__name = name
        self.__salary = salary
        self.__department= department

    # Protected method
    def _showdata(self):
        print(f'ชื่อพนักงาน : {self.__name}')
        print(f'เงินเดือน : {self.__salary}')
        print(f'ตำแหน่งงาน : {self.__department}')

# Object เรียกใช้งาน Class
obj1 = Employee("สมชาย",200,"Programmer")
obj1._showdata()