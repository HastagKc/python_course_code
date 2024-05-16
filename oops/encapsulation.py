#encapsulation---wrapping data(attribute) and method(function) that operate on data in singel entity

# class Student:
#     def __init__(self) -> None:
#         self.name="sujan"

#     def show(self):
#         print(f"my name  is {self.name}")

# a=Student()
# print(a.name)


# class B:
#     def show(self):
#         print(f" i m another class {a.name}")

# b=B()
# b.show()

# encapsultaion is used to restrict data and method from outside the class
#to acchive encapsultion we user access modifier
#public--data and method can be accessible other class
#private--data and method cannot be accessible from other class (__variable_name)
#protected=data and method can be accessible only in class and subclass(_variable)

class Student:
    def __init__(self) -> None:
        self.__name="sujan" #private variable
 
    def __show(self):
        print(f"my name  is {self.__name}")

    def display(self):
        self.__show()

a=Student()
# print(a._Student__name)
# print(a.__dict__)
# a.__show()
# a.display()

# class B(Student):
#     def show(self):
#         print(f"my another class name  {a.__name}")

# b=B()
# b.show()


# class Student:
#     def __init__(self) -> None:
#         self._name="sujan" #protect variable
 
#     def show(self):
#         print(f"my name  is {self._name}")

  

# a=Student()
# # print(a.__name)
# # a.__show()
# # a.display()
# print(a._name)

# class B(Student):
#     def show(self):
#         print(f"my another class name  {a._name}")

# b=B()
# b.show()


 