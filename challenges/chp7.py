#1
showsList = ['The Walking Dead', 'Entourage', 'The Sopranos', 'The Vampire Diaries']
for show in showsList:
    print(show)

#2
for i in range(25,51):
    print(i)

#3
showsList = ['The Walking Dead', 'Entourage', 'The Sopranos', 'The Vampire Diaries']
for i, show in enumerate(showsList):
    listNumber = str(i)
    print('Number #'+listNumber+": " + show)

#4
listOfNumbers = [6, 11, 37, 2026, 999, 2]
while True:
    checkNumber = input("Enter a number to check if it is in the list (or 'q' to quit):")
    if checkNumber == 'q':
        break;
    else:
        try:
            checkNumber = int(checkNumber)
            if checkNumber in listOfNumbers:
                print('It is in the list!')
            else:
                print("It is not in the list!")
        except ValueError:
            print('You did not enter a number!')

#5
listOne = [8, 19, 148, 4]
listTwo = [9, 1, 33, 83]
listThree = []

for itemOne in listOne:
    valueOne = itemOne
    for itemTwo in listTwo:
        valueTwo = itemTwo
        result = valueOne * valueTwo
        listThree.append(result)

print(listThree)