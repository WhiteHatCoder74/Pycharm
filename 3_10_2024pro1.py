class student:
    def __init__(self):
        self.no = 0
        self.name = ""
    def setdata(self):
        self.no = int(input('Enter number::'))
        self.name = input('Enter name::')
    def printdata(self):
        print("no =", self.no, "name = ", self.name)


n=int(input("Enter limit =>"))

list1=[]
for i in range(1,n+1):
    s1=student()
    s1.setdata()
    list1.append(s1)


for x in list1:
    x.printdata()
