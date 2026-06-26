#1

class Square():
    def __init__(self, s):
        self.sideLength = s

    def perimeter(self):
        return self.sideLength * 4
    
class Rectangle():
    def __init__(self, l, h):
        self.length = l
        self.height = h

    def perimeter(self):
        return (self.length * 2 ) +  (self.height * 2)
    

shape1 = Square(4)
shape1 = str(shape1.perimeter())
print("Square perimeter is: " + shape1)

shape2 = Rectangle(4, 5)
shape2 = str(shape2.perimeter())
print("Rectangle perimeter is: " + shape2)

#2
class Square():
    def __init__(self, s):
        self.sideLength = s

    def perimeter(self):
        return self.sideLength * 4
    
    def changeSizeBy(self, n):
        self.sideLength = self.sideLength + n
    
shape = Square(4)
output = str(shape.perimeter())
print("Square perimeter is: " + output)

shape.changeSizeBy(-5)
output = str(shape.perimeter())
print("Square perimeter is now: " + output)

class Shape():

    def __init__(self):

        self.shape = ''

    def whatAmI(self):

        if(self.shape == 'Square'):
            print('I am a square')
        elif(self.shape == 'Rectangle'):
            print("I am a rectangle")
        else:
            print("I am a shape")

class Square(Shape):
    def __init__(self, s):
        self.shape = 'Square'
        self.sideLength = s

    def perimeter(self):
        return self.sideLength * 4
    
class Rectangle(Shape):
    def __init__(self, l, h):
        self.shape = "Rectangle"
        self.length = l
        self.height = h

    def perimeter(self):
        return (self.length * 2 ) +  (self.height * 2)

shape1 = Square(5)
shape1.whatAmI()
shape2 = Rectangle(10,3)
shape2.whatAmI()
shape3 = Shape()
shape3.whatAmI()

#4 - pasted from: https://github.com/calthoff/tstp/blob/master/part_II/the_four_pillars_of_oop/challenges/chall_4.py

class Rider():
    def __init__(self, name):
        self.name = name


class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

the_rider = Rider("Sally")
harry_the_horse = Horse("Harry", the_rider)

print("The name of Horse is {}".format(harry_the_horse.name))
print("The name of Rider is {}".format(harry_the_horse.rider.name))