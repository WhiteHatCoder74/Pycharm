# private, pubic and protected data members
# private data members can be accessed anywhere
# public data members can be accessed only inside or for that specific class
# protected data members can be accessed only for that specific class as well as only for it's one previous parent class.


class Dada:
    def __init__(self):
        self.a=2
        self.__b=5
        self._c=3
    def printdata(self):
        print("A = ",self.a," B = ",self.__b," C = ",self._c)

class Papa(Dada):
    def __init__(self):
        self.d=10
        self.__e=20
        self._f=30
    def printdata(self):
        Dada.__init__(self)
        print("C = ",self._c , self.a)
        print("D = ",self.d," E = ",self.__e," F = ",self._f)

class Child(Papa):
    def __init__(self):
        Papa.__init__(self)
        self.mul=0
    def multi(self):
        self.mul= self.d * self._f
        print("Multi = ",self.mul)

c1=Child()
c1.d=33
c1.multi()