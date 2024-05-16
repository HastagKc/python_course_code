#four fundamental concept in oops
#inheritance
#polymorphism
#encapcuslation
#abstraction


#inheritance---class that derived all method and attribute in another class 
# parent class----base class
# child class ----> derived class


#single inheritance
# class A: #parent class
#     def fet1(self):
#         print("i have a feature one ")

# class B(A): #child class
    
#     def fet2(self):
#         print("i have a feature 2")


# # a=A()
# # a.fet1()
# # a.fet2()

# b=B()
# b.fet2()
# b.fet1()

#single level or multi-level inheritance

# class A: #grand parent
#     def fet1(self):
#         print("i have a feature one ")

# class B(A): #parent
    
#     def fet2(self):
#         print("i have a feature 2")

# class C(B): #child
#     def fet3(self):
#         print("i have a feature 3")



# a=C()
# a.fet1()
# a.fet2()
# a.fet3()


#multiple inheritance
# class A: #father
#     def fet1(self):
#         print("i have a feature one ")

# class B: #mother
    
#     def fet2(self):
#         print("i have a feature 2")

# class C(A,B): #child
#     def fet3(self):
#         print("i have a feature 3")

# a=C()
# a.fet1()
# a.fet2()
# a.fet3()

#hierachical inheritance
class A:
    def fet1(self):
        print("i have a feature one ")

class B(A):
    
    def fet2(self):
        print("i have a feature 2")

class C(A):
    def fet3(self):
        print("i have a feature 3")

a=C()
a.fet1()
a.fet3()

b=B()
b.fet1()
b.fet2()

#hybrid




