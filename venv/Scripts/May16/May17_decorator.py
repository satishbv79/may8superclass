# def f1():
#     def f2():
#         x=20
#         return x
#     return f2()
# a=f1()
# print(a)

#case 1:
def smarttv():
    print("smart tv")

def tv():
    print("normal tv")
tv()
smarttv()

#case 2

# def smarttv():
#     print("smart tv")
# @smarttv
# def tv():
#     print("normal tv")
# tv()
# smarttv()

#case 3

# def smarttv():
#     print("smart tv")
# @tv()
# def tv():
#     print("normal tv")
# tv()
# smarttv()

#case 4
# def smarttv():
#     print("smart tv")
#
# def tv():
#     print("normal tv")
# tv()
# smarttv()


#case 6

# def smarttv():
#     print("smart tv")
#
# def tv():
#     print("normal tv")
# tv()
# smarttv()


#case 7
# def smarttv(tv):
# #     print("smart tv")
# # @smarttv
# # def tv():
# #     print("normal tv")
# # tv()
# # smarttv()

def wtpv(smarttv):
    print("waterprroftv")
@wtpv
def smarttv(tv):
    print("stv")
@smarttv
deftv():
    print("inside tv")
tv()
