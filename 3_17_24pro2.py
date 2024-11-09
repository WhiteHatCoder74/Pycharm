#single inheritance
#private (e.g. --a, --b), public, protected


class india:
    def __init__(self):
        self._a=0
    def setindia(self):
        self._a = int(input("Enter student number: "))
    def printindia(self):
        print("a is",self._a)

class usa(india):
    def __init__(self):
        self.c=8
        self.__b = 0

    def setusa(self):
        self.__b = int(input("Enter b: "))

    def printusa(self):
        print("b is",self.__b)
    def printmulti(self):
        print("A times B is:",self._a*self.__b)

u1=usa()
u1.c
u1.setindia()
u1.printindia()
u1.setusa()
u1.printusa()
u1.printmulti()

