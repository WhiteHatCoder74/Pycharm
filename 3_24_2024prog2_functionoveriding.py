class person:
    def __init__(self):
        self.name=""
        self.language=""
    def setdata(self):
        self.name=input("Enter name: ")
        self.language=input("Enter language: ")
    def printdata(self):
        print("name is: ",self.name, "language is","self.language")
class emp(person):
    def __init__(self):
        self.designation=""
        self.salary=0
    def setdata(self):
        person.setdata(self) # this will take base class function
        self.designation = input("Enter designation: ")
        self.salary = int(input("Enter salary: "))
    def printdata(self):
        person.printdata(self) # this will take base class function
        print("Designation is:",self.designation, "Salary is:", self.salary)

e1=emp()
e1.setdata()
e1.printdata()

e1.setdata()
e1.printdata
