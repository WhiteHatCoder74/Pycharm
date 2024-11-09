class emp:
    def __init__(self):
        self.__eno=0
        self.ename=""
        self.esalary=0
    def setdata(self):
        self.__eno=int(input("Enter number: "))
        self.ename=input("Enter name: ")
        self.esalary=int(input("Enter salary: "))
    def printdata(self):
        print("Employee number is",self.__eno,"Employee name is", self.ename, "Employee salary is",self.esalary)

e1=emp()
e1.__eno=55

#e1.setdata()
#e1.printdata()
print(e1.__eno)