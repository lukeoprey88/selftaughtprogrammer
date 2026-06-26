#1
print("Hello, World")
print("I like Clare")
print("I also like swing dancing")

#2
x = 10

if x < 10:
    print("X is less than 10")
elif x >= 10:
    print("X is greater than or equal to 10")

#3
y = 1
try:
    y = int(y)
    if y <= 10:
        print("Y is less than or equal to 10")
    elif y <= 25:
        print("Y is greater than 10 but less than or equal to 25")
    elif y > 25:
        print("Y is greater than 25")
    else:
        print("I don't know what Y is")
except ValueError:
    print("Y is not an integer")

#4
x = 100
y = 6

result = x % y
print (result)

# 5
x = 100
y = 6

result = x // y
print (result)

#6 
age = 37
try:
    age = int(age)

    if age <= 2:
        print("You are very young")
    elif age> 2 and age <= 5:
        print("You are young")
    elif age > 5 and age <= 11:
        print("You are in primary school")
    elif age > 11 and age < 13:
        print("You are young")
    elif age >= 13 and age <= 19:
        print("You are teenager")
    elif age >= 20 and age < 65:
        print("You are an adult")
    elif age >= 65 and age < 199:
        print("You are a senior citizen")
    elif age > 200:
        print("You are extremely old")
    else:
        print("I don't know what age is being added. You're an alien")

except ValueError:
    print("Age variable is not an age")