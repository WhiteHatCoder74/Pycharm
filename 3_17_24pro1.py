#multilevel inheritance
#function overriding

class student:
    def __init__(self):
        self.studentnumber=0
        self.studentname=""
    def setdata(self):
        self.studentnumber = int(input("Enter student number: "))
        self.studentname = input("Enter student name: ")
    def printdata(self):
        print("student name is:", self.studentname, "student number is: ",self.studentnumber)


class marks(student):
    def __init__(self):
        self.english = 0
        self.hindi = 0

    def setdata(self):
        self.english = int(input("Enter english marks: "))
        self.hindi = int(input("Enter hindi marks: "))

    def printdata(self):
        print("english marks: ", self.english, "hindi marks: ", self.hindi)

class result(marks):
    def __init__(self):
        pass  # pass is used when no data member

    def printdata(self):
        print("Total marks: ", self.english + self.hindi)

r1=result()

r1.setdata()
r1.setdata()

r1.printdata()
r1.printdata()
r1.printdata()





