                                ###OBJECT ORIENTED PROGRMMING###

##Using List - Creating student records
# #Student Details

# student_1 = ['Pragya', 10]
# student_2 = ['Vibhuti', 12]

# student_3 = 'Avinash'
# student_1.append('A')

# print(student_1)

# print(f'{student_1[0]} is in class {student_1[1]}')
# print(f'{student_2[0]} is in class {student_2[1]}')


##USING OOPS


##CLASS - Blueprint/Template

#Student class created
#__init__ method - constructor, value initialized-fix
#self parameter - reference or help build connection btw class & object-fix


# class Student:                              #Student class            
#     def __init__(self, name, grade):        #this is method 1 
#         self.name = name                    #this is attribute (properties)
#         self.grade = grade


#     def student_details(self):              #method
#         print(f'{self.name} is in class {self.grade}')


#Object - Instance of class

# student1 = Student('Pragya', 10)
# print(student1.name, student1.grade)

# student2 = Student('Avinash', 12)
# print(student2.name, student2.grade)


# print(student1.name)
# student1.student_details()
# student2.student_details()

# #Student details in the form of dictionary
# print(student1.__dict__)

# #Modify existing object properties/attributes
# print(student1.grade)
# student1.grade = 11     #modify value
# print(student1.grade)


# # #Delete existing object properties/attributes

# print(student1.__dict__)
# del student1.grade
# print(student1.__dict__)


# # # #Delete existing object 
# del student1
# print(student1)





#-------------------------------------------------------------
##CREATE VARIABLE AND LINK IT TO OBJECT TO MAKE RELATION


##CLASS - Blueprint/Template


# class Student:                              #Student class            
#     def __init__(self, name, grade, percentage, team):        #this is method 1 
#         self.name = name                    #this is attribute (properties)
#         self.grade = grade
#         self.percentage = percentage
#         self.team = team


#     def student_details(self):              #method
#         print(f'{self.name} is in class {self.grade}, with {self.percentage} and is in team {self.team}')

# team1 = 'A'             #creating team(calue) to assign them with students
# team2 = 'B'



# #Object - Instance of class

# student1 = Student('Pragya', 10, 96, team1)
# # print(student1.name, student1.grade)

# student2 = Student('Avinash', 12, 99, team2)
# # print(student2.name, student2.grade)


# print(student1.team)
# student1.student_details()
# student2.student_details()






##---------------------##

# OOPs - Question

# Write a Python program to:

# Define a Student class with attributes name, grade, percentage, and team.

# Include an __init__ method to initialize these attributes.
# Add a method student_details that prints the student’s details in the format:
# "<name> is in <grade> grade with <percentage>%, from team <team>".
# Create two teams (team1 and team2) as string variables.

# Create at least two student objects, each belonging to one of the teams.

# Call the student_details method for each student to display their details.




                            ####OOPS FEATURES####

###4 features in OOPS which makes it more powerful. 
#Abstraction
#Encapsulation
#Inheritence
#Polymorphism



# ##ABSTRACTION - Hiding unnecessary details from users through method or class

# class Student:                              
#     def __init__(self, name, grade, percentage):        
#         self.name = name                   
#         self.grade = grade
#         self.percentage = percentage
     

#     def student_details(self):              #example of abstraction through method(hidden from users).   
#         print(f'{self.name} is in class {self.grade}, with {self.percentage+2}%')  


# #Object - Instance of class

# student1 = Student('Pragya', 11, 96)
# student2 = Student('Avinash', 12, 97)


# print(student1.percentage)
# student1.student_details()
# student2.student_details()


##ENCAPSULATION - Restrict access to certain attributes or methods to protect data and enforce controlled access.
#We use __ (double underscore) before attribute name after self. for encapsulation
#How to access attribute while encapsulated? - create new method to access, not directly.  

# class Student:                              
#     def __init__(self, name, grade, percentage):        
#         self.name = name                   
#         self.grade = grade
#         self.__percentage = percentage      ##double underscore limits access
     
#     def get_percentage(self):
#         return self.__percentage


#     def student_details(self):                
#         print(f'{self.name} is in class {self.grade}, with {self.percentage}%')  


# #Object - Instance of class

# student1 = Student('Pragya', 11, 96)
# student2 = Student('Avinash', 12, 97)


# # print(student1.percentage)      #error
# # print(student1.__percentage)    #error


# print(student1.get_percentage())




# ##INHERITANCE - Allows one class(child) to reuse the properties and methods of another class(parent). 

# ##PARENT CLAASS:
# class Student:                              
#     def __init__(self, name, grade, percentage):        
#         self.name = name                   
#         self.grade = grade
#         self.percentage = percentage     
     
#     def student_details(self):                
#         print(f'{self.name} is in class {self.grade}, with {self.percentage}%')  


# #Object - Instance of class

# student1 = Student('Pragya', 11, 96)
# student2 = Student('Avinash', 12, 97)

# ##CHILD CLASS:
# class GraduateStudent(Student):                #GraduateStudent child class inheriting the properties and methods from  Student parents class 
#     def __init__(self, name, grade, percentage, stream):    #old parametrs from parent class and new parameters in child class
#         super().__init__(name, grade, percentage)  #super is calling parent class init
#         self.stream = stream            #new attribute in child class

#     def student_details(self):
#         super().student_details()            #method inherit from parent class 
#         print(f'Stream is {self.stream}')
    

# #Object
# Grad_Student1 = GraduateStudent('Vibhuti', 12, 98, 'PCM') 
# #print(Grad_Student1.stream)


# Grad_Student1.student_details()




##POLYMORPHISM - Allows methods in different classes to have same name but different behavior depending on objects.

class Student:                              
    def __init__(self, name, grade, percentage):        
        self.name = name                   
        self.grade = grade
        self.percentage = percentage
     

    def student_details(self):                
        print(f'{self.name} is in class {self.grade}, with {self.percentage}%')  
        

#Object - Instance of class

student1 = Student('Pragya', 11, 96)
student2 = Student('Avinash', 12, 97)


##CHILD CLASS:
class GraduateStudent(Student):                 
    def __init__(self, name, grade, percentage, stream):    
        super().__init__(name, grade, percentage)  
        self.stream = stream            

    def student_details(self):          #method
        # print(f'{self.name} is in class {self.grade}, with {self.percentage} and from stream {self.stream}')
        print('same method with different o/p')

#Object - Student class
student1 = Student('Pragya', 11, 96)

#Object - GraduateStudent class
Grad_Student1 = GraduateStudent('Vibhuti', 12, 98, 'PCM') 


student1.student_details()
Grad_Student1.student_details()