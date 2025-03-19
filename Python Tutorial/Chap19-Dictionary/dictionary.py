                                        ###DICTIONARY###
#data str which stores data in key-value pair. 
#Dictionary items(key-value) are ordered, changeable and do not allow duplicates.
##key-value
#Key - must be unique and immutable(strings, numbers, tuples)
# #value - can be of any data type, does not need to be unique.

#Syntax:
#my_dict = {'key1':'value1', 'key2':'value2',....}


                                        ###METHODS TO CREATE DICTIONARY###
###create Using curly braces{}
# cohort = {'Course': 'Python', 'Instructor': 'Pragya', 'level': 'Beginner'}
# print(cohort)
# print(type(cohort))



###create Using dic() constructor 

# person = dict(name = 'Pragya', Age = '30', Grade = 'A')
# print(person)
# print(type(person))




###create Using list of Tuples 
#pass a list of tuples where each tuple contains key value pair.

# person2 = dict([('name', 'Pragya'), ('Age' , 30), ('Grade', 'A')])
# print(person2)
# print(type(person2))



                                 ###ACCESS DICTIONARY VALUES###

# #access distionary values by using key name inside square bracket.
# student = {1:'Masters', 'name': 'Pragya', 'grade': 'A', 'city': 'St. Paul'}
# print(student)
# print(type(student))


# print(student['grade'])
# print(student['name'])


                                ###DICTIONARY METHODS (BUILT-IN)###

##Useful Methods: .key()- return all the keys(list of keys), .values() -- return all the values, \
    # .items() - return all key-value pairs, .get() - return values for a key(with an optional default \
        # if key is missing)

# student = {1:'Masters', 'name': 'Pragya', 'grade': 'A', 'city': 'St. Paul'}

# #.key()

# print(student.keys())

# #.values()

# print(student.values())


# #.items()

# print(student.items())

# #.get()

# print(student.get('name'))


                            ###DICTIONARY - ADD, MODIFY, REMOVE ITEMS###

# student = {1:'Masters', 'name': 'Pragya', 'grade': 'A', 'city': 'St. Paul'}

##1. Add/Modify item: use asign-operator 

# #Add new key-value pair - assign operator
# student['email'] = 'pragya@gmail.com'
# print(student)


# #modify/replace an existing value - assign operator
# student["grade"] = 'A+'
# print(student)


##2. Remove item: use del or .pop to remove items from dictionary 

# #Remove with del
# del student["grade"]
# print(student)

# #remove with pop() and store removed value
# var1 = student.pop('email')
# print(var1)
# print(student)


                                    ###DICTIONARY ITERATIONS###


##Dictionary can be iterated using for loop.
#We can loop through distionaries by keys, values, or both.

student = {1:'Masters', 'name': 'Pragya', 'grade': 'A', 'city': 'St. Paul'}

# #Loop through Keys
# for key in student:
#     print(key)


# #Loop through values
# for values in student:
#     print(student[values])


# #Loop through values: using .values() method
# for values in student.values():
#     print(values)


# #Loop through both keys-values pair
# for keys, value in student.items():
#     print(keys,value)





                                     ###NESTED DICTIONARY###
# dictionaries inside dictionarie to store more complex data.
main_student = {
    'student1':{'name' :'Pragya', 'Age' : 30},
    'student2':{'name' :'Kako', 'Age' : 25, 'grade': 'A'} 
}

print(main_student)

#accessing the values
print(main_student['student1'])

#accessing the values
print(main_student['student2']['name'])


                                    ###DICTIONARY COMPREHENSIONS###
#Allows us to create dictionaries in a concise way.

#Syntax:
#new_dict = {key_expression : value_expression for item in iterable if condition}


squares = {x: x * x for x in range(1,6) }
print(squares)

my_dict = {x:x*x for x in range(1,10)}
print(my_dict)

my_dict2 = {x:x+x for x in range(1,10)}
print(my_dict2)
