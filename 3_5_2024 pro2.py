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


e1 = emp()
e2 = emp()
e3 = emp()


e1.setdata()
e2.setdata()
e3.setdata()

e1.printdata()
e2.printdata()
e3.printdata()
