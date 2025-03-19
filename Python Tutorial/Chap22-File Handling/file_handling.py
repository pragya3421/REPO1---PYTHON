                        ###FILE HANDLING###

#Mode: r -read, w - write, a - append

# #Open file

# file = open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example.txt", 'r')

##READ FILE##


# #Read 

# file = open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example.txt", 'r')
# content = file.read()       #read entire data
# print(content)
# # file.close()    #best practice


# #Readline 
# file = open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example.txt", 'r')
# content = file.readline()   #read first line
# print(content)
# file.close()


# #Readlines
# file = open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example.txt", 'r')
# content = file.readlines()   #list entire data
# print(content)
# file.close()


##WRITE TO A FILE##


# # #Write mode (overwrites)
# # file = open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example2.txt", 'w') #write mode
# # file.write("Hello and Namaste! My name is Pragya!!")
# # file.close()


# #Append mode (adds)
# file = open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example2.txt", 'a')
# file.write("\nHow are you?")
# file.close()


##CLOSE THE FILE##


#using with statement (no need to write 'close' statement)
with open(r"C:\PRAGYA\UST\COURSES\Python Tutorial\Chap22-File Handling\example2.txt", 'r') as file:
    content = file.read()
    print(content)







