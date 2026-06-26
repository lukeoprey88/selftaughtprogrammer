#1
import re

f = open('zen.txt', 'r')
text = f.read()

findText = re.findall('Dutch', text)

print(findText)

#2
string = 'Arizona 479, 501, 870. California 209, 213, 650'
findNumbers = re.findall("\d", string, re.IGNORECASE)
print(findNumbers)

#3
sentence = "The ghost that says boo haunts the loo"
findGhost = re.findall(".oo", sentence, re.IGNORECASE)
print(findGhost)