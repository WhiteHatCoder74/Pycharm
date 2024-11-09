#Hierarchical inheritance
class polygon:
    def __init__(self):
        self.h=0
        self.b=0
    def setpolygon(self):
        self.h = float(input("Enter h: "))
        self.b = float(input("Enter b: "))
    def printpolygon(self):
        print("h is:", self.h, "b is: ",self.b)


class Triangle(polygon):
    def __init__(self):
        pass # pass is used when no need for data member
    def printarea(self):
        print("area of tri = ",self.h*self.b*0.5)
class Rectangle(polygon):
    def __init__(self):
        pass
    def printarea(self):
        print("Area of rect = ",self.h*self.b)


t1=Triangle()
t1.setpolygon()
t1.printpolygon()
t1.printarea()


r1=Rectangle()
r1.setpolygon()
r1.printpolygon()
r1.printarea()