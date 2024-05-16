#mainly two type of programming langugae 
#procedural
#oops

#oops----object oriented programming language
#main conectp to map in real world scanarios

# Student form 
# Ram ----ram ko information
# syam---syam ko informtion

# oops use classs and object  to represent in real world entity or concept
#class ----blueprint of object,or template of creating object
#object---instance of class

#class is group of attribute and method
#attribute---it represent variable that contain data
#method---it is similar function,which perform certain task 

# syntax
# class Class_name:
#     pass

# a=Class_name() #object


# class Student:
#     def __init__(self):
#         self.name="sujan" 
#         self.age=44

#     def show(self):
#         print(self.name,self.age)

# a=Student()
# a.show()


class Student:
    def __init__(hello,name,age): #it is used to initalize the value on variable ,we donot need to call explicitly
        hello.abc=name
        hello.age=age

    def show(hello,price):
        hello.price=price
        print(f"my name is {hello.abc},our class price is {hello.price}")

    def display(hello):
        print(f"my age is {hello.age}")

R1=Student("sujan") #heap(dynamic memory)
# print(a.abc)#to call variable outside the class
R1.show(9876543)
R1.display()

R2=Student("ram") #self it s default variable (not a reserved keyword) which contain current object 
R2.show(987)


