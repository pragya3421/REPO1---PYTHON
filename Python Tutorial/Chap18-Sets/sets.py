                    ###SETS###

#collection of unique items in python.
#UNIQUE ELEMENTS- no duplicate values allowed.
#UNORDERED - no orer or sequesnce maintained, so no indexing.
#MUTABLE - can add or remove the elements after creation.
#IMMUTABLE ELEMENTS - individual elements in sets can not be modified/replaced.
#So, set is mutable but the elements in set are not mutable.
#Ex: vowels = {'a', 'e', 'i', 'o', 'u'}

                ##METHOD OF SET CREATION##

# #   Using curly braces {}

# my_set = {1,2,3,4,5}
# print(my_set)
# print(type(my_set))

# #Using set constructor ()

# my_set2 = set([1,2,3])
# print(my_set2)
# print(type(my_set2))

# Note: empty sets can not be created as it will be created as dictionary. We need to use set constructor to create empty set.


                        ##SET OPERATIONS##
# #Adding Element - add()
# numbers = {1,2,3,4}
# numbers.add(100)
# print(numbers)


##Remove Element - Remove() and discard()

#Remove
# fruits = {'apple', 'mango', 'banana'}
# fruits.remove('banana')       #if element not present, shows error.
# print(fruits)

# #Discard

# fruits.discard('apple')         #if element not present, does not shows error.
# print(fruits)



                            ##SET METHODS##

# #Union [.union()] - combines elements from two sets, removing duplicates.

# set1 = {1,2,3}
# set2 = {3,4,5}
# union_set = set1.union(set2)
# print(union_set)
#         #Note: Union alternative
# union_set2 = set1 | set2
# print(union_set2)    

# #Intersection [.intersection()] - includes only elements present in both sets(common elements).

# set1 = {1,2,3,4,5}
# set2 = {3,4,5}
# inter_set = set1.intersection(set2)
# print(inter_set)
#     #Note: intersection alternative
# inter_set2 = set1 & set2
# print(inter_set2)    

# #Difference [.difference()]- Elements present in first set but not in second set. 

# set1 = {1,2,3,4,100}
# set2 = {3,4,5}
# diff_set = set1.difference(set2)
# print(diff_set)

#     #difference alternative
# diff_set2 = set1 - set2
# print(diff_set2)

# #Symmetric Difference [.symmetric_difference()]: Elements in either set but not in both. 

# set1 = {1,2,3}
# set2 = {3,4,5,6}
# sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set)

#      #symmetric difference alternative
# sdiff_set2 = set1^set2
# print(sdiff_set2)


                                ##SET ITERATIONS##
#can use for loop to go through each element in a set. 

# #Using For loop - printing each number from a set.

# numbers = {1,2,3,4,5}
# for x in numbers:
#     print(x)

#Using while loop - set does not support while loop, we have to first converst a set into a list then use while loop because sets do not suppot indexing.



                            ##SET COMPREHENSIONS##
#Allows concise and readable creation of sets. Similar to list comprehensions but for stes. 
#new_set = {expression for item in iterable if condition}

# #Ex:
# squares = {x**2 for x in range(1,6)}
# print(squares)

# cube = {x**3 for x in range(1,6)}
# print(cube)

                        ##SET COMMON USE CASES##

##remove duplicate 
#Ex:
numbers = [1,2,3,4,5,6,6,8]
unique_numbers = set(numbers)
print(unique_numbers)

##membership testing - Quickly checks it an item is present in a collection.
##Set Operations - Perform mathematical operations like intersection, difference etc 
##Data Analysis - useful in scenarios requiring unique items such as tags, categories,  or unique identifiers.
 