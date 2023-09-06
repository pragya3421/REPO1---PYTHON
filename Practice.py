print("Hello World")
print("Hello Coders")
print("Hello Coders")
name = 'Pragya'
age = 22
print(name)
print(age)
name = "Amanda"
age = 24
print(name)
print(age)

## 4 types of variable - String/Integer/ Float and Boolean

is_adult = False

#EXERCISE
# - Add a person with the name Tony Stark
# - Tony's age is 51 years old.
# - Tony is a genius.

firstname = 'Tony'
lastname = 'Stark'
age = 51
is_genius = True

name = input("What is your name? ")
print("My name is " + name)

name = input("What is your superhero name? ")
print("Hello" + "My superhero name is " + name)

#Type conversion -

old_age = input("Enter your old age")
new_age = int(old_age) + 2
print(new_age)

first = input("enter first number")
second = input("input second number")
sum = int(first) + int(second)
print("The sum is " + str(sum))

## STRINGS

name = "Tony Stark"
name.upper()
print(name.upper())

name.lower()
print(name.lower())

#FIND operator - seerch S in Tony Stark - provides index no
print(name.find('stark'))
# replace  Tony Stark to IronMan

print(name.replace("Tony Stark", "IronMan"))
print(name)

#to check words existence in

print("T" in name)
print("M" in name)

#Arithmatic Operators

print(5+2)
print(5-2)
print(5/2)
print(5//2) #part after decimal gets removed
print(5%2) # remainder
print(5**2) # 5 to the power 2

#Shortcuts

i = 5
i = i + 2
i += 2
i -= 2
i *= 2

#Operator Precedence
#BODMAS
# / > * > + > -

result = 2 + 3 * 5
print(result)

#Comparison Operator

print(3>2)
print(3<2)
print(3<2)
print(3==2)
print(2==2)
print(3!=2)
print(3!=3)

#Logical Operators
#OR Operator
print(2>3 or 2<3)
#AND Operator
print(3>3 or 2>1)

#NOT Operator
print(not 2>3)

#IF-ELSE STATEMENT

age = 2

if age >= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are underage")
    print("You can not vote")

print("ThankYou")

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
elif age <18 and age > 3 :
    print("You are in school")
else:
    print("You are child")

print("ThankYou")

#MINI PROJECT - Lets build a calculator

first = int(input("enter first number: "))
operator = input("enter operator (+, -, *, /, %) : ")
second = int(input("enter second number: "))


if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")


#RANGE - range of numbers - going from one value to another value
#range(5) # 0, 1, 2, 3, 4

number = range(5)
print(number)

#LOOP
print(1)
print(2)
print(3)
print(4)
print(5)


#WHILE LOOP

i = 1
while i <=20:
    print(i * "*")
    i = i +1

i = 1
while i <=5:
    print(i * "Hello")
    i = i +1

i = 5
while i >=0:
    print(i * "*")
    i = i - 1

#FOR LOOPS - used to iterate over lists to take items from the number sequence.

#print 0-4
for i in range(5):
    print(i)

#print 1-5
for i in range(5):
    print(i + 1)

#LISTS
#collection of items - stores complex data types
#Ex - used to store marks in list

marks = [95, 99, 100]
print(marks)
print(marks[1])
print(marks[-1])
print(marks[0:2])
print(marks[1:3])

#In this list, put loop on each marks means access all the score

for score in marks:
    print(score)

#add another marks in this list - we will use append to add sth on end.

marks.append(99)
print(marks)

#add another marks in between on some index - we will use insert to add sth in between on some index.

marks.insert(0, 55)
print(marks)

marks.insert(3, 78)
print(marks)

# Check which element exists in our list
# 99 exists in our list or no?

print(99 in marks)

# check length of list
print(len(marks))

#ITERATE OVER LIST USING WHILE LOOP

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

#CLEAR LIST

marks.clear()
print(marks)

#BREAK & CONTINUE - at 1:01:29







