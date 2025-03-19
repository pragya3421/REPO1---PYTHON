                                        ###TUPLES###


#collection of items in python.
#(immutable)unchangeable, ordered and allow duplicate values. 
#Used to store multiple items in a single variable.

#Note: Ordered - Tuple items have a defined order, that order will not change.

                            ###CREATE TUPLE METHODS###


##1.Using Parenthesis

# my_tuple = (1,2,3)
# print(my_tuple)
# print(type(my_tuple))

# my_tupe1 = (1, "Pragya", "True", 3.16)
# print(my_tupe1)


##2.Without Parenthesis

# tuple1 = 1,2,3
# print(tuple1)
# print(type(tuple1))


##3.Using tuple constructor

# tuple2 = tuple((1,6,9))
# print(tuple2)
# print(type(tuple2))


# list1 = [1,2,3]
# new_tuple = tuple(list1)
# print(new_tuple)
# print(type(new_tuple))


##4.Create a single element


# b = ("b",)      #comma add
# print(b)
# print(type(b))


                                  ###ACCESS TUPLE USING INDEXING###

# fruits = ('apple', 'mango', 'cherry')
# print(fruits)
# print(type(fruits))

# print(fruits[0])
# print(fruits[-1])


                                    ###TUPLE SLICING###

# new_tuple = (10,20,30, 40, 50)
# print(new_tuple[0:3:1])
# print(new_tuple[0::2])
# print(new_tuple[0::3])


                                    ###TUPLE OPERATIONS###

##There are 3 Operations - Concatenation, Repetition, Checking for an item


##a. CONCATENATION - Join using +
# tuple1 = (1,2,3)
# tuple2 = ('a','b','c')
# tuple3 = tuple1+tuple2
# print(tuple3)


##b. REPETITION - using *
# tuple2 = ('a', 'b') *2
# print(tuple2)


##c. Checking for an item(element) in a tuple - Result in True or False
# my_tuple = (1,2,3)
# print(10 in my_tuple)
# print(2 in my_tuple)


                                        ###TUPLE ITERATION###

#for loop

# fruits = ('apple', 'mango', 'cherry')
# for x in fruits:
#     print(x)


#While Loop

# i = 0
# while i < len(fruits):
#     print(fruits)
#     i+=1


                                ###TUPLE METHODS###

# color = ('Blue', 'Green', 'Orange', 'Blue')

# #COUNT
# print(color.count('Blue'))

#INDEX
# print(color.index('Green'))

# print(color.index('Blue'))

                                ###TUPLE FUNCTIONS###

numbers = (1,2,3,4,5)

# #LEN

# print(len(numbers))

# #SUM

# print(sum(numbers))

# #MIN/MAX

# print(min(numbers))
# print(max(numbers))


# numbers2 = (1,5,3,7,2)


# print(sorted(numbers))              #tuple is now list
# print(sorted(numbers2))             #tuple is now list


# a = sorted(numbers2)
# numbers_sorted = tuple(a)
# print(numbers_sorted)



                                ###PACKING AND UNPACKING TUPLES###

# ##packing Tuple- putting multiple calues in single tuple.


# a = "Pragya"
# b = 22
# c = "Data Scientist"

# print(a,b,c)

# tuple_pack = a,b,c
# print(tuple_pack)

# ##Unpacking Tuple - extracting values from tuple into separate variables.


# name, age, profession = tuple_pack
# print(name)
# print(age)
# print(profession)

                         ###MODIFYING TUPLE###
###once tuple is created, we can not modify its elements. 


##Tuple modification
tuple_numbers = (10,20,30)

# tuple_numbers[0]=100      #error

##How to mutate/modify tuple

list_numbers = list(tuple_numbers)
print(list_numbers)

list_numbers[0] = 100
print(list_numbers)

tuple_numbers = tuple(list_numbers)
print(tuple_numbers)




##HW - try append, remove etc method. 


