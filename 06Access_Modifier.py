# การสร้าง Class และ Object
# Class
class Employee:
    # Method

    # Constructor
    def __init__(self,name,salary,department):
        # Protected attribute
        self._name = name
        self.__salary = salary
        self.__department= department

    # Protected method
    def _showdata(self):
        print(f'ชื่อพนักงาน : {self._name}')
        print(f'เงินเดือน : {self.__salary}')
        print(f'ตำแหน่งงาน : {self.__department}')

# Object เรียกใช้งาน Class
obj1 = Employee("สมชาย",200,"Programmer")
obj1.name = "DAlt"
print(obj1._name)
obj1._showdata()