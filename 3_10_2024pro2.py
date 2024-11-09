class emp:
    def __init__(self):
        self.eno =0
        self.ename=""
        self.salary=0

    def setdata(self):
            self.eno = int(input('Enter eno number::'))
            self.ename = input('Enter ename::')
            self.salary = int(input("Enter emp salary"))

    def printdata(self):
            print("eno =", self.eno, "ename = ", self.ename, "salary=", self.salary)


n=int(input("Enter limit =>"))

list1=[]
for i in range(1,n+1):
    s1=emp()
    s1.setdata()
    list1.append(s1)


for x in list1:
    x.printdata()