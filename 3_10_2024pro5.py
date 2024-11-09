#multiple inheritance
class student:
    def __init__(self):
        self.studentnumber=0
        self.studentname=""
    def setstudent(self):
        self.studentnumber = int(input("Enter student number: "))
        self.studentname = input("Enter student name: ")
    def printstudent(self):
        print("student name is:", self.studentname, "student number is: ",self.studentnumber)


class marks:
    def __init__(self):
        self.english = 0
        self.hindi = 0

    def setmarks(self):
        self.english = int(input("Enter english marks: "))
        self.hindi = int(input("Enter hindi marks: "))

    def printmarks(self):
        print("english marks: ", self.english, "hindi marks: ", self.hindi)

class result(student,marks):
    def __init__(self):
        pass  # pass is used when no data member

    def printotal(self):
        print("Total marks: ", self.english + self.hindi)

r1=result()
r1.setstudent()
r1.setmarks()

r1.printstudent()
r1.printmarks()

r1.printotal()

