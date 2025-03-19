###Arguments in Function

##Required Arguments (single/multiple)

# def greetings(name):     #name is Parameter 
#     print("Hello:", name, "!")

# greetings("Pragya")   #Pragya is argument
# greetings()           #argument required to run the code


# def intro(course_name, instructor_name):
#     print("Welcome to", course_name, "course by", instructor_name)

# intro("Python", "Pragya!")

##Default Arguments (single/multiple)

# def greetings(name = 'World'):
#     print("Hello,",name,"!")

# greetings()             #runs without using default value
# greetings('Pragya')     #runs without using default value


##Keyword Arguments(named arguments)
# def divide(a,b):
#     return a/b

# result1 = divide(10,5) #positional argument
# print(result1)

# result2 = divide(a = 10,b = 5)  #keyword argument
# print(result2)

# result3 = divide(b = 10,a = 5)
# print(result3)

###Arbitrary Arguments - variable length arguments *args and **kwargs

##Arbitrary positional arguments (*args)
#Note-Stores arguments as tuple.


# def add2numbers(a,b):
#     return a + b

# result = add2numbers(10,11)
# print(result)



# def add3numbers(a,b,c):
#     return a + b + c

# result1 = add3numbers(10,11,12)
# print(result1)



# def add_numbers(*args):
#     print(type(args))
#     return sum(args)

# result = add_numbers(5,10,10,30) #the arguments are stored as tuple.
# print(result)



# def greetings2(*names):
#     for name in names:
#         print(f"Hello, {name}!")

# greetings2("Pragya", "Vibhuti")





##Arbitrary keyword arguments (**kwargs)
#The arguments are stored as a dictionary.
#used when you want to pass multiple values that are accessed by name.


def print_details(**kwargs):
    #print(type(kwargs))   #Dictionary type
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(name = "Pragya", Age = 26, City = "Delhi")
print_details(name = "Pragya", Age = 26)



