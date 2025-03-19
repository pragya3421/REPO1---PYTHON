#                                 ###LISTS IN PYTHON###    

# ###1CREATE LIST


# # my_list = [1,2,3]
# # print(my_list)
# # print(type(my_list))

# # my_list2 = [1, "Pragya", 2, "John" ,3.14]
# # print(my_list2)
# # print(type(my_list2))

# # my_list3 = [1, 2, [3,4],"John",8.5, ["Banana", "Apple"]]
# # print(my_list3)
# # print(type(my_list3))


# ###2.ACCESS LIST - INDEXING (Access only one element in List)

# list1 = [10,30,50,66,90]

# print(list1[3])
# print(list1[-2])


# ###3.LIST SLICING - (Access more than one element in List)
# #Access range of element in a List.

# ##Syntax:  list_name[start:stop:step]

# numbers = [100, 200, 300, 400, 500, 600]

# #Slice from index 1 to 3.
# print(numbers[1:4])

# #Slice from start to  index 2.
# print(numbers[0:3])
# print(numbers[:3])

# #Last 3 elements
# print(numbers[-3:])


# #Slice all alternate elements.
# print(numbers[0::2])

# #Reverse List
# print(numbers[::-1])

##Slice with negative indices


# Slice the last three elements
# print(numbers[-3:])  # Output: [50, 60, 70]

# Slice everything except the last two elements
# print(numbers[:-2])  # Output: [10, 20, 30, 40, 50]

# Get a sublist from the third last to the second last element
# print(numbers[-3:-1])  # Output: [50, 60]

# Reverse the list using slicing
# print(numbers[::-1])  # Output: [70, 60, 50, 40, 30, 20, 10]

# Extract every second element from the last five elements
# print(numbers[-5::2])  # Output: [30, 50, 70]


###4.MODIFYING LIST  -
#lists are mutable(changeable), change their content after creation. 
#Add, remove, or change elements in a list.

# fruits = ["Banana", "Apple", "Peach", "Lemon"]
# print(fruits)


#a. Changing(modify) list 
# fruits[2] = "Blueberry"

# print(fruits)

#b. Adding and element (add single element to the end of list)

# fruits.append("Mango")

# print(fruits)


#c. removing an element

# fruits.remove("Banana")

# print(fruits)


                                                ###5.LIST METHODS  ###

# # append(): Adds a single element to the end of the list.

# fruits = ["Banana", "Apple", "Peach", "Lemon"]
# print(fruits)


# fruits.append("Cherry")
# print(fruits)


# fruits.append(110)

# print(fruits)


# # extend(): Adds multiple elements (from another iterable) to the end of the list.

# fruits = ["Banana", "Apple", "Peach", "Lemon"]
# another_fruits = ["Orange", "Tomato", "Avacado"]        #another list
# fruits.extend(another_fruits)
# print(fruits)



# # insert(): Inserts an element at a specified position or index.

# fruits = ["Banana", "Apple", "Peach", "Lemon"]
# fruits.insert(1, "Blueberry")
# print(fruits)




# # remove(): Removes the first occurrence of a specified element.

# fruits = ["Banana", "Apple", "Peach", "Lemon", "Apple"]
# fruits.remove("Apple")
# print(fruits)




# # clear(): Removes all elements from the list, resulting in an empty list.

# fruits = ["Banana", "Apple", "Peach", "Lemon", "Apple"]
# fruits.clear()
# print(fruits)



# # pop(): Removes and returns an element at a specified index. If no index is specified, it removes and returns the last element.

# numbers = [10, 20, 30, 40, 50]
# popped = numbers.pop(2)       
# print(popped)
# print(numbers)


# # pop() with default: pops last value by default

# numbers = [10, 20, 30, 40, 50]
# last = numbers.pop()       
# print(last)
# print(numbers)


# # finding index(): (Finding Index) Returns the index of the first occurrence of a specified element.


# fruits = ["Banana", "Apple", "Peach", "Lemon", "Apple"]
# index = fruits.index("Apple")
# print(index)


# # Finding index(): (Finding Index) within a range.

# fruits = ["Banana", "Apple", "Peach", "Lemon", "Apple"]
# index = fruits.index("Apple", 2)
# print(index)



# # count(): Returns the number of occurrences of a specified element.

# fruits = ["Banana", "Apple", "Peach", "Lemon", "Apple"]
# count = fruits.count("Apple")
# print(count)



# # reverse(): Reverses the elements of the list in place.

# fruits = ["Banana", "Apple", "Peach", "Lemon", "Apple"]
# fruits.reverse()
# print(fruits)


# # sort(): Sorts the list in ascending order by default. You can also sort in descending order and specify custom sorting criteria.

# #Asc order - 
# numbers = [100, 50, 80, 20, 90]
# numbers.sort()       #default sort in  asc order
# print(numbers)

# #Desc order - 
# numbers = [100, 50, 80, 20, 90]
# numbers.sort(reverse = True)       
# print(numbers)

# #Sorting with Key- 
# fruits = ["Banana", "Apple", "Peach", "Pomagranate", "Blueberry"]
# fruits.sort(key=len)        #sort based on length   
# print(fruits)

# #Sorting with Key- 
# fruits = ["Banana", "Apple", "Peach", "Pomagranate", "Blueberry"]
# fruits.sort(key=len, reverse=True)        #sort based on length   
# print(fruits)




# # copy(): Copying list - Returns a shallow copy of the list.

# fruits = ["Banana", "Apple", "Peach", "Pomagranate", "Blueberry"]
# copy_fruits = fruits.copy()    
# print(fruits)
# print(copy_fruits)



# #modifying the copy does not affect the original list.

# copy_fruits.append("Mango")    
# print(copy_fruits)
# print(fruits)

                                                ###JOIN LISTS### 

# ##JOIN or CONCATENATE Lists

# list1 = [1,2,3]
# list2 = ["a","b"]

# Using + operator

# final_list = list1 + list2

# print(final_list)


# #using append method

# for x in list2:
#     list1.append(x)

# print(list1)


# #using extend method

# list1.extend(list2)

# print(list1)



                                             ###LISTS COMPREHENSIONS### 

#concise way to create a list.
#Syntax 
#my_list = [expression for item in iterable if condition]
#Main COmponent of List comprehension - expression, for clause, if condition (optional) 

#Create a list of Squares:

# squares = [x**2 for x in range(1,6)]
# print(squares)


#filter even numbers:

# even_list = [x for x in range(1,10) if x%2==0]
# print(even_list)

#apply function to element of a list

# my_name = "Pragya"
# print(my_name)
# print(my_name.upper())
# print(my_name)


# my_list = ["Apple", "Mango", "Cherry"]
# print(my_list)
# print(my_list.upper())            #wrong way


# my_list = ["Apple", "Mango", "Cherry"]
# print(my_list)

# upper_list = [lst.upper() for lst in my_list]
# print(upper_list)



#Flatten a nested list using list comprehension method

# nested_list = [[1,2], [3,4], [5,6]]

# result = [item for sublist in nested_list for item in sublist]

# print(result)

##OR


# def flatten_list(lst):
#     return [item for sublist in lst for item in sublist]
 
# final_list = flatten_list(nested_list  )
# print(final_list)

                                        ###LISTS ITERATIONS### 



fruits = ['apple', 'mango', 'cherry']

# #Using for loop:

# for x in fruits:
#     print(x)
print(len(fruits))

#Using While loop:


index = 0
while index < len(fruits):
    print(fruits[index])
    index+=1

