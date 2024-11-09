class student:
    def __init__(self,no,name): #consructorwith parameter
        self.no= no
        self.name=name
    def printdata(self):
        print("number is",self.no, "name is", self.name)

s1=student(1,"raj")
s2=student(2,"simran")
s3=student(3,"neha")
s1.printdata()
s2.printdata()
s3.printdata()