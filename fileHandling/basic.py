#file handling 
#file ---it it used to collect data and  information to store permanently 
#file two types :
#text file : used to store in the form character Eg : .txt,.py,
#binary file  :used to store in the form of byte :.pdf,.png,.mp3


# file handling ---it is used to perform such as creating,read,write,delete and append

# open()
# perform one that file 
# close()
#this process is called file handling

# syntax:
# funtion_object=open("file_path","mode")

# f=open("msg.txt","x") #create

# mode---purpose of opening file 
#r --read
# f=open("msg.txt","r")
# b=f.read(20)
# b=f.readline()
# b=f.readlines()
# print(b)

#w--write
# f=open("msg.txt","w")
# f.write("welcome")
# f.write("\nk xa")

#a--append
# f=open("msg.txt","a")
# f.write("this is for append")

#w+,r+,a+
# f=open("msg.txt","r+")
# b=f.read()
# print(b)

#
# f=open("C:/Users/Sujan/Desktop/file/m.txt","r")
# b=f.read()
# print(b)
# f.close()
# #data corrupt
# #memeory wastage

# print("some code")

# try:
#     f=open("C:/Users/Sujan/Desktop/file/m.txt","r")
#     b=f.read()
#     print(b)
# finally:
#     f.close()


# with statement

# with open("msg.txt",'r') as f:
#     print(f.read())
#     print(f.closed)
# print(f.closed)
# import os
# # f=open("msg.txt",'r')
# os.remove("msg.txt")


#tell ---it tell current position of curser
#seek  --it change the position of curser
f=open("msg.txt",'r')
# print(f.tell())
# print(f.read(10))
# f.seek(0)
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# print(f.read(10))
# f.seek(23)
# b=f.read(10)
# print(b)

# import keyword
# print(keyword.kwlist)

# class A:
#     def __init__(self):
#         self.__x = 42
# class B(A):
#     def __init__(self):
#         super().__init__()
# b = B()
# print(b.__x)
