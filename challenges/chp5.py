'''
#1
favouriteMusicians = ["Van Morrison", "Norah Jones", "Tommy Emmanuel"] #list - ordered
print(favouriteMusicians)

#2
stMalachys = "54.59361385713068, -5.924057959798726"
eileenHowell = "54.59981346005676, -5.944680216706274"
boatClub = "54.56931945297502, -5.927303875022463"
locationsIMetClare = (stMalachys, eileenHowell, boatClub) #tuple - unchanging values
print(locationsIMetClare)

#3
myAttributes = {
    'height': '5"11',
    'eyeColour': 'blue',
    'glasses': True
} #dictionary - key:value requirement
print(myAttributes)

#4
dictionaryEntry = input("Please enter a key to search in my attributes: ")

try:
    if dictionaryEntry:
        dictionaryCheck = myAttributes[dictionaryEntry]
    else:
        dictionaryCheck = 'Key not found'

    print(dictionaryCheck)

except KeyError:
    print('Key not found')
'''
#5
favouriteMusicians = {
    'Van Morrison': ['Days Like This', 'Bright Side of the Road'],
    'Norah Jones': ['Come Away With Me', 'Sunrise'],
    'Tommy Emmanuel': ['Angelina', 'Guitar Boogie']
}
print(favouriteMusicians['Van Morrison'])