                                    ### LOOPS IN PYTHON - NESTED LOOP###
#Lopps inside another loop



#SYNTAX BELOW-

#outer_loop :
#    inner_loop:
#        #block of code for inner loop
#block of code for outer loop

##Example
# print numbers from 1 to 3 using nested loop

# for number in range(1,4):
#     print(number)

# # print numbers from 1 to 3 (3times)

# for number in range(1,4):
#     print(number)

# for number in range(1,4):
#     print(number)

# for number in range(1,4):
#     print(number)




print("___________________________________")
# print numbers from 1 to 3 for (3times)

# for i in range(3):
#     print ("Iteration no:", i)
#     for num in range(1,4):
#         print(num)


# print("=========")
## print numbers from 1 to 3 using while loop

# i = 1

# while i < 4:
#     print("While loop iteration no - ", i)
#     for j in range(1,4):
#         print(j)
#     #print("- - - - - - -- ")
#     i +=1


print("Prime Numbers")
##print prime numbers between range of 2 to 10 using nested loops.

for num in range(2,20):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)