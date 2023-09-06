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

#USING BREAK
students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

#USING CONTINUE

for student in students:
    if student == "kishan":
        continue;
    print(student)

#TUPLE - Like List but it is immutable.
#We can not modify tuple like list. We can not use insert, append, clear in tuble.
#we can not assign items on any index.
#Use parenthesis
#It counts which object is how many times

marks = (95, 98, 97, 97, 99)
print(marks.count(97))

# In tuple, there is no need to use parenthesis. We get the elements in tuple format only if we print. The print result will be in the format of tuple only.
#Ex -
person = "Jack", "Karen", "Connor", "Alanna"
print(person)

#see index of no.
print(marks.index(95))

#SETS
#We use curly braces for set.
#Since we do not have indexes in sets, it is called unordered.

# #We need to store so many elements but want to keep only unique elements and not duplicates.
# If there are repetition of element in set, only unique value and one element from duplicate will get printed.


marks = {95, 98, 97, 97, 97}
print(marks)

#There is no existence of indexes in sets.
marks = {95, 98, 97, 97, 97}
print(marks[0])

#We can not iterate over or access values using indexes in sets. We can only use loops to access the values or elements of sets.
for score in marks:
    print(score)


##DICTIONARY
#used to store key value pair
#for single student with pair key information.

#To access the single information, we write whole key in place of index number.
#Key will be used as index.
marks = {"english" : 95, "chemistry" : 98}
print(marks["chemistry"])

#Add new marks
marks["physics"] = 97
print(marks)

#CHANGE MARKS
marks["physics"] = 99
print(marks)

##FUNCTIONS
#In-Built Functions
#Module Functions
#User-defined functions


#In-Built Functions - int(), str(), bool()

#Module Functions
#Ex - Math module
import math
print(dir(math))

from math import sqrt
print(sqrt(4))

from math import *  #* is used to get all the functions
print(sqrt(4))

#User-defined functions
#Syntax below

def function_name(parameters):
    //do something
#________________________________
def print_sum(first, second):
    print(first + second)

print_sum(1, 2)

#__________________________________________
def print_sum(first, second=4):
    print(first + second)


print_sum(1)

#_____________________________________
def print_sum(first=3, second=4):
    print(first + second)


print_sum()
#_______________________________________


##########
#Programming/Placements/Compatative Programming - Python (OOPS)
#Machine Learning/Data Science - File Handling
#Development - Django Framework


















