###PYTHON PROGRAM TO CREATE SIMPLE CALCULATOR

##Write a Python program to create a calculator that can perform at least five different mathematical\
#  operations such as addition, subtraction, multiplication, division, and average. Ensure\
#  that the program is user-friendly, prompting for input and displaying the results clearly.

##TASKS:
#   Step1.Create functions
#   Step2.User Input
#   Step3.Print Result

#   Step1.Create functions

#ADD TWO NUMBERS
def add(num1, num2):
    return num1 + num2

#SUBTRACT TWO NUMBERS
def sub(num1, num2):
    return num1 - num2

#MULTIPLY TWO NUMBERS
def multiply(num1, num2):
    return num1 * num2

#DEVIDE TWO NUMBERS
def divide(num1, num2):
    return num1 / num2

#AVERAGE TWO NUMBERS
def avg(num1, num2):
    return (num1 + num2)/2

#   Step2. User Input

print("Please select a operation:\n" \
    "1.Addition\n" \
    "2.Subtraction\n" \
    "3.Multiply\n" \
    "4.Divide\n" \
    "5.Average")

select = int(input("Select a operations from 1-5: "))

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: 3"))


#  Step3.Print Result

if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))

elif select == 2:
    print(number1, "-", number2, "=", sub(number1, number2))

elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))

elif select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))

elif select == 5:
    print("(", number1, "+", number2, ")", "/", "2", "=", avg(number1, number2))

else:
    print("Invalid Operation! Please select again..")