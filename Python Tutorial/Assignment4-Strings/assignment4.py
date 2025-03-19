#1. Limit the decimal places to 2 digits using .format and print result, for the variable pi =  3.14159265359

pi =  3.14159265359
print(round(pi,2))

print("Value of Pi is {}".format(pi))
print("{}".format(pi))

#using f-function formatting float numbers
print("Value of Pi is {:.2f}".format(pi))
print("{:.2f}".format(pi))


#Using f-strings
print(f"{pi:.2f} using f-string")


##2. extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8 , skipping every other char.

my_string = "Python Course"

#String [start:stop:step]

print(my_string[2:8:2])


##3. Slice to get only the middle character(s): For my_string1 = "Pragya", use slicing to extract the middle  character(s). 

my_string1 = "Pragya"  #6 characters - even

my_string2 = "Madhavi"  #7 characters - odd
#index:0123456

def mid_str(word):
    middle = int(len(word)/2)            # 3
    if len(word) % 2 == 0:              #even character length
        return word[middle-1:middle+1]  #2:4
    else:                               #odd character length
        return word[middle]
    
print(mid_str(my_string1))
print(mid_str(my_string2))


##4. Remove the first 3 and last 3 characters: Given my_string = 'Regression Analysis', \
# remove the first 3 and last 3 characters.

my_string3 = "Regression Analysis"
print(my_string3[3:-3])


##5. Get the substring that starts 4 characters from the end to the last characters: \
# For my_string4 = "Classification", slice the string starting from 4th characterts from the \
# end to the last characters. 

my_string4 = "Classification"
print(my_string4[-4:])

##6. How to reverse a string using Python string method. 
word = "Python"
print(word[::-1])

##7. Write a Python function to check id a string is a palindrome  using string methods.

word = "Madam"
word1 = "Madan"

def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a Palindrom")
    else:
        print(f"{s} is not a Palindrom") 

is_palindrome(word)   
is_palindrome(word1)  


#8 and 9 are homework :)

#8. Difference Between find() and index() in Python? 

#9. Efficient String Concatenation method: Why is using join() often more efficient than using + for string concatenation in a loop? 