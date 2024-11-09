class student:
    def __init__(self):
        self.sno=0
        self.name=""

    def setdata(self):
        self.sno=int(input("Enter student number: "))
        self.name=input("Enter student name: ")
    def printdata(self):
        print("Student number is: ", self.sno, "Student name is: ", self.name)

class marks(student):
    def __init__(self):
        self.english=0
        self.hindi=0
    def setdata(self):
        self.english = int(input("enter english marks: "))
        self.hindi = int(input("enter hindi marks: "))
    def printdata(self):
        print("english grade is: ",self.english, "hindi grade is",self.hindi)

m1=marks()
m1.setdata()
m1.printdata()

m1.setdata()
m1.printdata()