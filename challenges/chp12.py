import math

#1
class Apple():
    def __init__(self, color, weight, datePicked, locationPicked):
        print('Apple class created!')

Apple('red',10,'Monday', 'Seville')

#2

class Circle():

    def __init__(self, r):
        self.radius = r

    def area(self):
        area = math.pi * (self.radius * self.radius)
        areaString = str(area)
        print('The area of this circle is: ' + areaString)

circleRadius = input("Please insert a radius to find the area of: ")
circleRadius = int(circleRadius)
circle1 = Circle(circleRadius)
circle1.area()

#3

class Triangle():

    def __init__(self, b, h):
        self.base = b
        self.height = h
        
    def area(self):
        area = 0.5 * self.base * self.height
        areaString = str(area)
        print('The area of this triangle is: ' + areaString)

triangleBase = int(input("Please insert a base to find the area of: "))
triangleHeight = int(input("Please insert a height to find the area of: "))

triangle1 = Triangle(triangleBase, triangleHeight)
triangle1.area()

#4
class Hexagon():

    def __init__(self, s):
        self.side = s
        
    def area(self):
        area = (3 * math.sqrt(3) * (self.side ** 2)) / 2 # https://www.educative.io/answers/how-to-get-the-area-of-a-hexagon-in-python
        areaString = str(area)
        print('The area of this hexagon is: ' + areaString)

hexagonSide = int(input("Please insert a length of side to find the area of: "))

hexagon1 = Hexagon(hexagonSide)
hexagon1.area()