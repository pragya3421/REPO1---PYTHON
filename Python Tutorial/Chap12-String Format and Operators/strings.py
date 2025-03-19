###STRINGS IN PYTHON - PART 1
##Strings - chars in single, double and triple quotes.


# name = "Pragya"  #creating a string
# Age = 16

# print(name)
# print(type(name))  #checking data type

# print('Hello World!')

# print("Hello World!")
# print("It's Easy!")

# print("Quotes")

# print(''' "Quotes" ''')

# print(" \"Quotes\" ")   #Escape sequence

##Foramatted Strings - insert variable or expressions
#1. Old Style Formatting - % Operator

# name = "Pragya"
# age = 16
# print("My name is %s and I'm %d yrs old!" % (name,age))
#%s,  %d are placeholders for string and integer



#2. Str.Format method  / str.format() method

#SYNTAX: "string {}".format(value)

# name = "Pragya"
# age = 16
# print("My name is {} and I'm {}".format(name, age))

# # you can reference variables by index or keyword
# print("My name is {0} and I'm {1}".format(name, age))
# print("My name is {1} and I'm {0}".format(name, age))
# print("My name is {name} and I'm {age}".format(name = "Pragya", age = "18"))

##3. Formatted Strings - F-strings
#SYNTAX: f"string {variable}"

# name = "Pragya"
# age = 20
# print(f"My name is {name} and I'm {16} yrs old!")
# print(f"In 5 Yrs, I will be {age+5} yrs old!")

###ESCAPE CHARACTERS

#Escape characters in Python are special characters  used in strings to represent whitespace, symbols, \
# or control characters that would otherwise be difficult to include.
# It is a backslash\ followed by the character you want to insert.

# print(''' "Quotes" ''')

# print(" \"Quotes\" ")  #print double quotes using backslash.
# print(" \'Quotes\' ")   #print single  quotes using backslash.
# print("Hello \nWorld")  #new line
# print("Hello \tWorld")  #tab  = space



###STRING OPERATORS IN PYTHON

# a = "Hello"
# b = "Python"
# print(a+b)  #concatenate
# print(a*2)  #multiple copies
# [] - slice, [:] - range   ----scroll below

# if "H" in a:            #In Operator (Case sensitive)
#     print("Yess")
# else:
#     print("No")


# if "h" in a:            #In Operator (Case sensitive)
#     print("Yess")
# else:
#     print("No")


# if "h" not in a:            #Not In Operator
#     print("Yess")
# else:
#     print("No")


# print("Hello\nWorld")       #New Line
# print(r"Hello\nWorld")      #r(raw string) - suppress esape characters 



# String Indexing, Slicing and methods in PART 2 


