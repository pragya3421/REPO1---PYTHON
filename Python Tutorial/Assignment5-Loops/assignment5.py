                                        ###ASSIGNMENT - 5###

## Print the while loop output in same line
# print("Hello", end = " ")
# print("Madhav")

#
# print("Hello", "Pragya", sep = "*", end = " * ")
# print("Madhav")


#
# i = 1
# while i < 4:
#     print(f"Hello Pragya {i}", end = " ")
#     i += 1

# print("======================")

#
# i = 1
# while i < 4:
#     print(f"Hello {i}", "Pragya", sep = "*", end = " ")
#     i += 1


##2 Print star patterns – using loops

#
n = 5       #No of rows

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end = " ")
#     print()


#
# for i in range(1,n+1):
#     print("*" *i)


##3 Print star patterns (inverted triangle) – using loops

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()


# for i in range(n,0, -1):
#     print("* " *i)


##4 Print pyramid patterns – using loops

n = 5   #no of rows

# for i in range (1, n+1):            #for loop for no of rows
#     print(' ' * (n-i), end = "")    #spaces to center the starts
#     print("*" * (2 * i - 1))        #print stars


##5 Write a program to find the factorial of a given number

# def factorial(n):

#     result = 1
#     while n > 0:
#         result*=n       #result = n*result
#         n -= 1
#     return result

# print(factorial(5))



##6 Count the number of vowels in a string

# my_string = "Welcome!Python by Pragya Verma"
# vowels = "aeiou"

# count = 0
# for char in my_string:
#     if char.lower() in vowels:
#         count+=1
# print("Number of vowels : ", count)    



##7 Find the longest word in a sentence using a for loop.

# sentence = "Welcome! Python by Pragya Verma"

# words = sentence.split()

# longest_word = ""

# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print("The longest word is:", longest_word)


# for word in words:
#     print(word)



##8 "do-while" loop in Python – how to do it?

# while True:
#     num = int(input("Enter a number greater than 10:"))

#     if num > 10:
#         print(f"Valid number entered: {num}")
#         break #exit loop when condition satisfies
#     else:
#         print("Number is not greater than 10, Try again!")







##9 Write a program to print first N numbers in the Fibonacci sequence using a while loop.
#Each number is equal to the sum of the preceding two numbers. Ex: 0112358... 

def fibonacchi(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a)        #0 1 1 2 3
        a,b = b, a+b
        count += 1      #0 1 2 3 4

fibonacchi(5)

