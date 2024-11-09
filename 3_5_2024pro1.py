class student:
    def __init__(self):
        self.no = 0
        self.name = ""
    def setdata(self):
        self.no = int(input('Enter number::'))
        self.name = input('Enter name::')
    def printdata(self):
        print("no =", self.no, "name = ", self.name)


s1=student()
s2=student()
s3=student()

s1.setdata()
s2.setdata()
s3.setdata()

s1.printdata()
s2.printdata()
s3.printdata()
