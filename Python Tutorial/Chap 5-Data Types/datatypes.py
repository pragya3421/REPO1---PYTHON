#data types in python

a = 1
b = 1
print(a)
print(a+b)
print(type(a)) #type: integer

c = "1"
d = "1"
print (c+d)

print(type(c)) #data type: string 

##Data type in Python

##NUMERIC

a1 = 1  #integer
print(type(a1))

a2 = 1.5 #float
print(type(a2))

a3 = complex(3,5) #complex
print(type(a3))

##SEQUENCE

b1 = "Pragya"  #string
print(type(b1)) 

b2 = [1,4,7,26,'Pragya']  #list
print(type(b2))

b3 = (1,4,7,26,'Pragya')  #tuple
print(type(b3))

##DICTIONARY - key-value pair Ex= json file

my_dictionary = {'name': 'Pragya', 'Age' : 30, 'City' : 'Kansas'}
print(my_dictionary)
print(type(my_dictionary))

##SETS 
my_sets = {1,4,7,26,'Pragya'}
print(type(my_sets))

##BOOLEAN

bool1 = True
bool2 = False
print(type(bool1))

##BINARY
#binary, bytearray, memoryview
byte1 = b"Pragya"
print(type(byte1))
