###Operators in Python

##1. Arithmatic Operators
# a = 5
# b = 3
# print (a+b) #addition operator
# print (a-b) #substraction operator
# print (a*b) #multiplication operator
# print (a%b) #modulus operator


##2. Comparison Operators = Output is boolean value T/F
# a = 5
# b = 3
# print(a>b) #greater than
# print(a<b) #less than
# print(a==b) #equal to operator
# print(a!=b) #not equal to operator

##3. Assignment Operators 
# a = 5   #assignment operator

##4. Logical Operators 
#Rule for 'and' operator
#a. T + T = True
#b. T + F = False
#c. F + F = False

a = 10
b = 20
# print(a==10 and b <10) #AND Operator
# print(a==10 and b==20) #AND Operator


#Rule for 'or' operator
#a. T + F = True
# a = 10
# b = 20
# print(a==10 or b<20) #OR Operator


#'not' operator
# print(not(a==10 and b==20))


##5. Identity Operators - is, is not

# x = [1,2,3]
# y = x
# z = [1,2,3]

# print(x is y) # is operator
# print(x is z)

# print(x is not z) # is not operator


##6. Membership Operators - in, not in

# my_list = ['apple', 'orange', 'watermelon']
# print('apple' in my_list)  #in operator
# print('mango' in my_list)

# print('mango' not in my_list)  # not in operator


##6. Bitwise Operators(works on binary numbers 0,1) - AND(&), OR (|), XOR(^), NOT(~) etc
a = 5           #  5 in binary - 0101
b = 3           #  3 in binary - 0011
print(a & b)    #  1 in binary - 0001

#Rule for  AND '&' operator
#a. T + T = True
#b. T + F = False
#c. F + F = False