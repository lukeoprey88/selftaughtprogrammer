#1
def numberSquared(x=1):
    """
    Returns x squared.
    :param x: int.
    :return int x squared
    """
    return x*x

print(numberSquared(2))
print(numberSquared())

#2
def printString(x = "Nothing supplied"):
    """
    Returns a print of the supplied string.
    :param x: str.
    :return printout of x
    """
    return print(x)

printString("I wonder what's for dinner")
printString()

#3
def threeAndTwo (x, y, z, message = "Text not supplied", sound = 'Parf'):
    print(x, y, z, message, sound)

threeAndTwo('Number 1', 'Next', 'Argh')

#4
try:

    suppliedInteger = input("Supply a number to divide in half and then quadruple:")

    suppliedInteger = int(suppliedInteger)

    def divideInHalf(suppliedInteger):
        return suppliedInteger // 2

    def quadruple(y):
        return y * 4
    
    first = divideInHalf(suppliedInteger)
    second = quadruple(first)
    print (second)

except ValueError:
    print("Y is not an integer")

#5
def stringToFloat (inputString):

    try:
        inputString = float(inputString)
        print("Float: ", inputString)

    except ValueError:
        print("An integer was not supplied")

inputString = input("Supply a integer to turn into a float                                                      :")
stringToFloat(inputString)