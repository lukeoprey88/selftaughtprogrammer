#1

philosopher = 'Camus'
'''
print(philosopher[0])
print(philosopher[1])
print(philosopher[2])
print(philosopher[3])
print(philosopher[4])
'''
for character in philosopher:
    print(character)

#2
message = input("What was the message? ")
recipient = input("Who was the message for? ")
combined = "Yesterday I wrote: {}. I sent it to: {}".format(message, recipient)
print(combined)

#3
birthYear = 'aldous Huxley was born in 1894'
birthYear = birthYear.capitalize()
print(birthYear)

#4
message = "Where now? Who now? When now?"
messageList = message.split('? ')

i = 0; # start loop counter
for line in messageList:
    if i < (len(messageList)-1):
        messageList[i] = line + '?' # add ? back, but not on last one
        i+=1

print(messageList)

#5
fox = ['The', 'fox', 'jumped', 'over', 'the', 'fence.'];
foxMessage = ' '.join(fox)
print(foxMessage)

#6
dollarSwitch = "A screaming comes across the sky."
dollarSwitch = dollarSwitch.replace('s', '$')
print(dollarSwitch)

#7
mFind = 'Hemingway'
mFind = mFind.find('m')
print(mFind)

#8

#9
threeWays = 'three ' + 'three ' + 'three'
print(threeWays)
threeWays = 'three ' * 3
print(threeWays)

#10
sliceString = 'It was a bright cold day in April, and the clocks were striking thirteen.'
sliceStringPosition = sliceString.find(',')
sliceString = sliceString[0: sliceStringPosition]
print(sliceString)