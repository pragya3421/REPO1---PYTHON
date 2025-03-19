##LOOPS IN PYTHON

###WHILE LOOP

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1

##Q Print numbers from 1-5 using while loop
# count = 1
# while count < 6:
#     print(count)
#     count += 1


# count = 10
# while count > 0:
#     print(count)
#     count -= 1



# count = 10
# while count > 0:
#     print(count)
#     count -= 1
# else:
#     print("While loop ended")





# while True:
#     print("Its infinite loop")


 
# count = 10
# while count > 0:
#     print(count)
#     count += 1
# else:
#     print("While loop ended")


##Check conditions to avoid infinite loop!




###FOR LOOP


# language = "Python"

# for x in language:
#     print(x) 


##FOR LOOP WITH RANGE FUNCTION

# range(stop)
# range(start,stop,step)

# for i in range(5):                #stop argument 
#     print(i)

# for i in range(7,11,1):             #start, stop and step argument
#     print(i)



# for i in range(5):
#     print(i)
# else:
#     print("For loop ended")



###LOOP CONTROL STATEMENTS

##Allows us to alter the normal flow of a loop.

#3Clauses
#-Pass Statement
#-break statement
#-continue statement


#PASS STATEMENT

# for i in range(5):
#     #do not run it now
#     pass



# count = 5
# while count > 0:
#     if count == 3:
#         pass
#     else: 
#         print(count)
#     count -= 1



#BREAK STATEMENT

# for i in range(5):
#     if i ==3:
#         break
#     print(i)


#CONTINUOUS STATEMENT

# for i in range(5):
#     if i ==3:
#         continue
#     print(i)





# count = 5
# while count > 0:
#     if count == 3:
#         pass
#     else: 
#         print(count)
#     count -= 1

# print("---------")



##Do not try at home - its infinite loop
# count = 5
# while count > 0:
#     if count == 3:
#         #continue
#     else: 
#         print(count)
#     count -= 1



while True:
    user_input = input("Enter 'exit' to STOP: ")
    if user_input == 'exit':
        print("Congrats! You guessed it right!")
    break
print("Sorry! You entered: ", user_input)