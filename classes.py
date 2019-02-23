import math 
class Orange :
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("created")

class Apple:
    def __init__(self,a,c,w,t):
        self.age = a
        self.color = c
        self.weight = w
        self.taste = t

class Circle:
    def __init__(self,r):
        self.radius = r

    def calc_Circum(self):
        return math.pi * (self.radius**2)

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def calc_area(self):
        return (self.base * self.height) / 2

or1 = Orange(10,"dark orange")
print(or1.weight)
print(or1.color)

ap1 = Apple("old","red",6,"sour")

print(ap1.age)

circ1 = Circle(3)

print("The area of circle with radius {} is {}".format(circ1.radius, circ1.calc_Circum()))

tri1  = Triangle(5,4)

print(tri1.calc_area())
