#exception handling---the process of responding unexcepted event occur when program is run 

# try:
#     def show(a):
#         print("hello sipalaya")

#     show()
# except:
#     print("error occur")

# print("some imp code is here")


#error
#mainly three types
#syntax error
# def show(a):
#         print("hello sipalaya")

# show()

#run time error
# def show():
#         a="sujan"
#         print(a[9])

# show()

#ZeroDivisionError
#Name error
#value error
#type error
#index error


#logical error
# def show():
#     print(2*3)
# show()



# try:
#     def show():
#         a="sujan"
#         print(3/2)
#         print(2+2)
#         print(a[2])

#     show()

# except IndexError:
#     print("your index error is occur")

# except TypeError:
#     print("your type is not match")

# except ZeroDivisionError:
#     print("you shouldnot divide by zero")

# except:
#     print("error occur")


# finally:always excuted

# try:
#     def show():
#         a="sujan"
#         print(a[9])

#     show()

# except:
#     print("error occur")

# finally:
#     print("hello sipalaya")


def show():
    try:
        print(2/0)
    except:
        print("error occur")
        return 1
    finally:
        print("hello sipalaya")

show()
        