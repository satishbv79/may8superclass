#Exception Handling
# print("program started")
# def m1():
#     a=10
#     b=0
#     c=a/b
#     print(c)
# m1()
# print("program ended")

# case 1
# print("program started")
#
# def m1():
#     try:
#         a = 10
#         b = 0
#         c = a / b
#         print(c)
#     except:
#         print("zeroDivision")
#
#
# m1()
# print("program ended")

#case 3

# print("program started")
#
# def m1():
#     try:
#         a = 10
#         b = 0
#         c = a / b
#         print(c)
#     except: Exception as e:
#         print(e)
#
#
# m1()
# print("program ended")

# case 6 -- error

# print("program started")
#
# def m1():
#     try:
#         a = 10
#         b = 0
#         c = a/b
#         print(c)
#     except zeroDivisionError as e:
#         print(e)
#     except TypeError as e:
#         print(e)
#     except Exception as e:
#         print("in exception ",e)
#
# m1()
# print("program ended")


# case Try & Else


# print("program started")
#
#
# def m1():
#     try:
#         a = 10
#         b = 'a'
#         c = a / b
#         print(c)
#     else:
#     print(" in else block")
#
#
# m1()
# print("program ended")

#case try & finally
# print("program started")
#
#
# def m1():
#     try:
#         a = 10
#         b = 'a'
#         c = a / b
#         print(c)
#     else:
#     print(" in else block")
#
#
# m1()
# print("program ended")

#case nested try
print("program started")


def m1():
    try:
        a = 10
        b = 10
        c = a / b
        print(c)
        try:
            print("inside try block --try")
        except:
            print("inside try block -- except")
        else:
            print("inside try block -- else")
        finally:
            print("inside try block -- finally")
    except Exception as e:
        print("in exception ", e)
    else:
        print(" in else block")
    finally:
        print("inside finally")


m1()
print("program ended")
