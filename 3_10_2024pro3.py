#single inheritance

class usa:
    def __init__(self):
        self.a=0

    def setusa(self):
        self.a=int(input("Enter number for usa:"))

    def printusa(self):
        print("a is",self.a)


class japan(usa):  #relationship between two classes
    def __init__(self):
        self.b=0

    def setjapan(self):
        self.b=int(input("Enter number for japan:"))

    def printjapan(self):
        print("b is",self.b)

    def printmulti(self):
        print("A*B = " ,self.a*self.b)

j1=japan()

j1.setusa()
j1.setjapan()
j1.printusa()
j1.printjapan()
j1.printmulti()





