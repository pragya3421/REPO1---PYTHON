#casting in python 
a = 1
print(type(a))

b = "1"
print(type(b))


c = int(b)

print(type(c))

print(a+c)

print(a+int(b))

name = "Pragya"

#All numerical values can be casted as string but not all the strings can be casted to numerical type. 
mynum = 25
mynum2 = str(mynum)

print(type(mynum2))


f1 = 22.56
print(type(f1))

print(type(int(f1)))

f2 = int(f1)
print(f2)
print(type(f2))

in1 = 26
print(type(in1))

in2 = 27
print(type(float(in2)))


### IMPLICIT CASTING

var1 = 10
var2 = 15.5
var3 = var1+var2
print(var3)
print(type(var3))

##Explicit type casting
int_num = 101
str_num = str(int_num)
print(type(str_num))

a0 = bool(0)
print(a0)
print(type(a0))

a1 = bool(1)
print(a1)
print(type(a1))


