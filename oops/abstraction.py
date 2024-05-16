#abstraction---the process of hiding data from the user and show only services
# print("hello world")




# from hide import summation
import hide
hide.summation()
# print(summation(2,6))
# print(sum([2,6]))

from abc import ABC,abstractmethod

class Student(ABC):

    @abstractmethod  #abstact method
    def show(self):
        pass

class B(Student):
    def show(self):
        print("hello this is show abstact method")
    def display(self):
        print("hello sipalaya this is another class")

a=B()
a.display()
