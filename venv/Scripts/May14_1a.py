# #case 1:positional arguments
# def sum_of_num(x,y):
#     z=x+y
#     print(z)
# sum_of_num(2,3)

#case 2: default arguments

# def f1(a,b,c=20,d=30):
#     print(a,b,c,d)
# f1(1,2,3,4)


# def f1(a,b,c=20,d=30):
#     print(a,b,c,d)
# f1(1,2,3)

# def f3(a,b,c=20,d=30):
#      print(a,b,c,d)
# f3(1,2)

# def roi(p,t,r):
#     r=(p*t*r)/100
#     print(r)
# roi(1000,2,3)

# def roi(p,t,r):
#     r=(p*t*r)/100
#     print(r)
# #roi(1000,t=2,r=3)
# #roi(1000,r=3,t=2)
# #roi(r=3,t=2,1000)  # positional argument follows keyword argument --error
# #roi(r=3,1000,t=2) # positional argument follows keyword argument --error
# roi(p=1000,t=2,r=3)


# case4 : keyword arguments with default arguments

# def f1(a,b,c=30,d=40):
#     print(a,b,c,d)
# #f1(c=300,d=400,a=1,b=2)
# #f1(a=1,b=2,c=300,d=400)
# f1(a=1,b=2,c=300)

#case 5 : variable arguments

# def f1(*x):
#     print(x)
#     s = 0
#     for i in x:
#         s = s + i
#         print(s)
# #f1(2,3)
# #f1(2,3,4)
# f1()

#case 6 variable arguments with default arguments & positional arguments

# def f1(a,b=20,*x):
#     print(a,b)
#     for i in x:
#         print(i)
# #f1(10,200,3,4)
# #f1(10,100,200)


#case 7 function return types

# def f1(a, b):
#     c = a + b
#     print(c)
#     return c
#
#
# d = f1(2, 3)
# print(d)

def f1(a,b):
    c=a+b
    print(c)
    return
d=f1(2,3)
print(d)

