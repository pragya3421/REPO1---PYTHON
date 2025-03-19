###STRING INDEXING

##Index: 012345

# my_name = "Pragya"
# print(my_name[0])       #1st character of string
# print(my_name[-1])       #Last character of string

# name2 = "Hello World!"
# print(name2[0])
# print(name2[1])
# print(name2[2])
# print(name2[3])
# print(name2[4])
# print(name2[5])
# print(name2[6])
# print(name2[7])
# print(name2[8])
# print(name2[9])
# print(name2[10])
# print(name2[11])

# print(name2[-1])

###STRING SLICING

#It helps accessing part of the sequence in Python.
#Helps to het subset of characters from string using specified range of indices.

#Syntax: strint[start:end:step]
    #start: the index to start slicing (inclusive).Default value is 0.
    #end: the index to stop slicing (exclusive). Dafault value is length of string.
    #step: How much to increment the index after each character. Default value is 1.


# my_name = "Pragya Verma"
# print(my_name[0:6])
# print(my_name[0:6:1])
# print(my_name[7:12:1])

# print(my_name[0:2])
# print(my_name[0:3])
# print(my_name[2:5]) #3rd to 5th
# print(my_name[1:4]) #2rd to 4th
# print(my_name[-1:]) #Last Character
# print(my_name[11:]) #Last Character
# print(my_name[-2:]) #Last two Character
# print(my_name[-3:]) #Last three Character
# print(my_name[0::2]) #every 2nd character/alternative character - step count 2
# print(my_name[:]) #all character
# print(my_name[::]) #all character
# print(my_name[:-1]) #reverse string order
# print(my_name[::-1]) #reverse string order


###STRING METHOD

word = "Hello, Pragya is good"
#1. len()
print(len(word))

#2. upper()
print(word.upper())

#3. lower()
print(word.lower())

#4. count()
print(word.count('a'))

#5. find()
print(word.find('a'))

#6. split()
print(word.split(','))
print(word.split())

#7. replace()
print(word.replace('Hello','Hi'))

#8. title()
print(word.title())

#9. strip()
word2 = "  Hello World   "
print(len(word2))
print(word.strip())

#10. join()
zwords = "Pragya ", "is", "Great"
print(" ".join(zwords))
print(" -".join(zwords))




