                        ###Assignment - 6 (List, Tuple, Set, Dict)###
##1. Find the Intersection (common elements) of Two Lists---------------------------------------
# list1 = [1,2,3,4,5,6,7]
# list2 = [4,5,6,7,8,9,10]

# #using for loop:

# def intersection_loop(list1, list2):
#     common_list = []
#     for item in list1:
#         if item in list2 and item not in common_list:
#             common_list.append(item)
#     return common_list

# print(intersection_loop(list1, list2))



# #Using List Comprehension

# def intesection_comp(list1, list2):
#     return [item for item in list1 if item in list2]

# print(intesection_comp(list1, list2))


# #2. Find the Most Frequent Element in a List-------------------------------------------------------

# numbers = [1,2,2,3,4,4,4,4,5,6,8,9,9]

# def most_freq(list):
#     max_count = 0
#     most_freq = None
#     for item in list:
#         count = list.count(item)
#         if count > max_count:
#             max_count = count
#             most_freq = item

#     return most_freq

# print(most_freq(numbers))




# #3. Find Cumulative Sum of a List

# numbers = [1,2,3,4,5]

# def cumulative_sum(list):
#     cum_sum = []
#     total = 0
#     for  num in list:
#         total += num
#         cum_sum.append(total)
#     return cum_sum
# print(cumulative_sum(numbers))




##4. Remove Duplicates from a List – 2 methods

fruits = ["apple", "banana", "cherry", "apple", "banana", "strawberry"]

#using loop




# Find the index of an element in a tuple




# Find the Most Frequent Value in a dictionary




# Merge Dictionaries with Summation




# Flatten a Nested Dictionary




# Sort a Dictionary by Values




# Access values from a nested dictionary