#input function in python

# a = input()
# print(int(a)+int(a))

#input fucntion always reads  input value as string

# name = input("Enter Your Name:" )
# print(f"Welcome {name} to the Python from Pragya Verma")
  

# age = input("Enter Your Age: ")
# print(f"Oh! You are just {age}")
# print(f"So next Year you will be {int(age)+1}!")

# #Input from User to add two numbers and print the result.
# x = input("Enter first number: ")
# y = input("Enter second number: ")
# print(f"Sum of {x} and {y} is {int(x)+int(y)} ")


#HW: Write a program to input student name and marks of 3 subjects.
#print name and percentage in output.

# stu_name = input("Hi! Enter your name: ")
# b = input("Enter Python Marks:")
# c = input("Enter SQL Marks: ")
# d = input("Enter Tableau Marks: ")
# #calculate percentage
# percentage = ((int(b)+int(c)+int(d))/300)*100

# #print result
# print(f"Hi {stu_name}! The percentage of your marks is {int(percentage)}%. Well Done!")



# ##OPTIMIZED SOLUTION
# print("PERCENTAGE CALCULATOR")
# stu_name = input("Hi! Enter your name: ")
# b = int(input("Enter Python Marks:"))
# c = int(input("Enter SQL Marks: "))
# d = int(input("Enter Tableau Marks: "))
# #calculate percentage
# percentage = ((b+c+d)/300)*100

# #print result
# print(f"Hi {stu_name}! The percentage of your marks is {percentage}% Well Done!")


##WRITE A PROGRAM THAT COLLECTS MULTIPLE TYPES OF DATA TO STORE IN A DICTIONARY AND PRINT OUTPUT.


# #Usual input from user
# name = input("Enter Your name: ")  
# age = input("Enter Your age: ")  
# height = input("Enter Your height: ")  
# student = input("Are you a student (Yes/No): ")


#initializing a dictionary
user_data = {}

#input from user in distionary
 
#way to write key and value (as input) in a distionary
user_data['name']= str(input("Enter Your name: "))  #Key & Value
user_data['age']= int(input("Enter Your age: "))  #Key & Value
user_data['height']= float(input("Enter Your height: "))  #Key & Value
user_data['student']= str(input("Are you a student (Yes/No): "))  #Key & Value

#Print input from user
print(user_data)
