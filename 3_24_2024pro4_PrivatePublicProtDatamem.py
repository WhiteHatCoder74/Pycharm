class Test:
    def __init__(self):
        self.__a = 1 # private data member
        self.a1=20 # public data member


    def printa(self):
        print("A = ",self.__a," A1 = ",self.a1)

t = Test()

t.printa()

t.a1=33
t.printa()

t.__a=25 # as __a is private data member it cannot be accessed outside class. That is why line #18 will not print A = 25
t.printa()

