##CONDITIONAL STATEMENT IN PYTHON

##1. if statement

# a = 26
# b = 108
# if condition:
#     print("")

# a = 26
# b = 108
# if b>a:
#     print(" b is greater that a")

##If statement works only for True condition.

# a = 260
# b = 108
# if b>a:
#     print(" b is greater that a")

# age = 26
# if age  > 19:
#     print(" You are an adult")

# age = int(input("Enter Your Age: "))
# if age  > 19:
#     print(" You are an adult")


##2. if-else statement
#provides alternative block of code to execute if the condition is false.
#if-else handles false condition.

# age = int(input("Enter Your Age: "))
# if age  > 19:
#     print(" You are an adult")
# else:
#     print("You are a child")


# temp =  30
# if temp  < 25:
#     print(" Its a cool day")
# else:
#     print("Its Hot Day!")


##3. if-elif-else statement
#checks multiple condition and execute different block of codes based on which condition is true. 


marks = int(input("Enter your Marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# else: 
#     print("Grade: C")


##4. nested if-else statement
#places an if-else statement inside another if-else statement. 
#Allows for more complex decision making by checking multiple conditions that depend on each other. 

#Ex: number classification 
#classify a number as positive, negative  or zero and further classify as even or odd.

number = int(input("Enter a number: "))

if number > 0: #checking positive number 
    if number % 2 == 0:
        print("This is a even number")
    else:
        print("This is an odd number")
else:
    if number == 0: # checking zero value 
        print("This is zero")
    else:
        print("This is a negative number")


# 5. Conditional Expressions (ternary operator)
 
age = 16 
status = "Major" if age >= 18 else "Minor"
print(status)
    