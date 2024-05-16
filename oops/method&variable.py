#class---it is group of attribute(variable) and method

#attribute ---it represent variable which contain data 
#method --it is used perform a task or action

#types of attribute  ---instance variable,class variable/static variable
#type of method --instance method,class method,static method

# instance variable --variable whose separated copy of file is created for every object
#it is defined and initialize using constructor with self parameter


# class Student:
#     def __init__(self,name) -> None:
#         self.name=name  #instance variable

#     def show(self):  #instance method which is used to access instance variable
#         print(f"my name is {self.name}") #inside the class,self.variable_name

# a=Student("sujan")
# # print(id(a))
# a.name="ajay"
# a.show()

# b=Student("ram")
# b.show()
# print(id(b))

# a=Student("sujan")
# a.show()
# print(id(a))



# print(a.name) #object.variable_name
# a.name="ram"
# print(a.name)
# # a.show()



# R1=Student("sujan")
# R1.name="syam"
# R1.show()

# R2=Student("ram")
# R2.show()


# class variable :variable whose single copy of file is created for every object
#define and initialize using contructor with cls parameter

# class Student:
#     School="mangala"  #class variable
#     def __init__(self,name) -> None:
#         self.name=name

#     def show(self,pr):
#         self.School=pr
#         print(f"my name is {self.School}")

#     @classmethod
#     def display(cls,pr):
#         cls.School=pr
#         print(f"my school name is {cls.School}") #class variable access cls.variable_name

# a=Student("sujan")
# print(Student.School) # Class_name.variable_name
# # 
# a.show("united")
# # a.display("united")
# print(Student.School) # Class_name.variable_name




# class Student:
#     School="mangala"  #class variable
#     def __init__(self,name) -> None:
#         self.name=name

#     def show(self):
        
#         print(f"my name is {self.name}")

#     @classmethod
#     def display(cls):  
#         print(f"my school name is {cls.School}") #class variable access cls.variable_name

# a=Student("sujan")
# Student.School="united"
# a.display()

# b=Student("ram")
# b.display()



# staticmethod


# def show(a,b):
#     print(a+b)

# show(2,3)
class Student:
    @staticmethod
    def show(a,b):
        print(a+b)


a=Student()
a.show(2,3)
