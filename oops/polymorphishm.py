#polymorphism----one thing behave in many form 
#poly --many  morphism-form

# a="sujan"
# b="ram"
# print(a)

#duck type
# class A:
#     def show(self):
#         print("i want to learn python ")

# class B:
#     def show(self):
#         print("i want to learn django")

# kshitiz=A()
# # kshitiz.show()

# suresh=B()
# # suresh.show()
# def display(var):
#     var.show()

# display(kshitiz)
# display(suresh)


# method overloading --class contain more than one method with same name but different paramenter

# class A:
#     def show(self):
#         print("hello sipalaya")

#     def show(self,a,b):
#         print("sum of a and b is ",a+b)

#     # def show(self,a,b,c):
#     #     print("sum of a ,b , c is ",a+b+c)


# a=A()
# a.show()

# class A:
#     def show(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None and c==None:
#             s=a+b
#         elif a!=None and b==None and c==None:
#             s=a 
#         elif a==None and b==None and c==None:
#             s="hello sipalaya there is no data"
#         else:
#             s="j sukai gar"

#         return s
    
# a=A()
# print(a.show(1,2,3))


#method overriding--whenever we write the same name method in parent class and child class

# class A:
#     def show(self):
#         print("this is parent class")

# class B(A):
#     def show(self):
        
#         print("this is child class")
#         super().show()


# ob=B()
# ob.show()

#super() --this is inbuilt method which is used to access the parent method

#operator overloading

# a=[1,2,3,4]
# b=[1,2,3]
# print(a+b)

class A:
    def __init__(self,x) -> None:
        self.x=x

    def __add__(self,other):
        return self.x +other.y
    
class B:
    def __init__(self,y) -> None:
        self.y=y

a=A("2")
b=B("2")
print(a+b)


