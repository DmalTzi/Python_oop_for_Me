# การสร้าง Class และ Object
# Class
class Employee:
    # Method

    # Constructor
    def __init__(self,name,salary,department):
        # Protected attribute
        self.__name = name
        self.__salary = salary
        self.__department= department

    # Protected method
    def _showdata(self):
        print(f'ชื่อพนักงาน : {self.__name}')
        print(f'เงินเดือน : {self.__salary}')
        print(f'ตำแหน่งงาน : {self.__department}')

    # Setter method
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary

    def setDepartment(self,newdepartment):
        self.__department = newdepartment

    # Getter method
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

# Object เรียกใช้งาน Class
obj1 = Employee("สมชาย",200,"Programmer")

print("Name : {}".format(obj1.getName()))
print("Salary : {}".format(obj1.getSalary()))
print("Department : {}".format(obj1.getDepartment()))