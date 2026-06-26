'''
#1 and #2
class Square():

    squareList = []

    def __init__(self, s):
        self.side = s
        self.squareList.append(s)

    def __repr__(self):
        side = str(self.side)
        return side + ' by ' + side + ' by ' + side + ' by ' + side

square1 = Square(1)
print(Square.squareList)
square2 = Square(7)
print(Square.squareList)
square3 = Square(98)
print(Square.squareList)

print(square1)
print(square2)
print(square3)
'''
#3
class Pen():
    def __init__(self):
        pass

class Pencil():
    def __init__(self):
        pass

def areTheyTheSame(item1, item2):

    if (item1 is item2):
        print("They are the same")
    else:
        print("They are not the same")


test1 = Pen()
test2 = Pen()
test3 = Pencil()

areTheyTheSame(test1, test2)
areTheyTheSame(test2, test3)
areTheyTheSame(test1, test3)
areTheyTheSame(test1, test1)