class student:
    def __init__(self): #consructor without parameter
        self.no= 2
        self.name="rohan"
    def printdata(self):
        print("number is",self.no, "name is", self.name)

s1=student()
s2=student()
s3=student()
s1.printdata()
s2.printdata()
s3.printdata()