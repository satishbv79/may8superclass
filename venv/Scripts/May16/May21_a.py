# print even numbers _1
# for var in range(0,100,2):
#     print(var)

# i=3
# print(i**2)

#square root of 1 to 10 -- type1_2a
# l=[1,2,3,4,5,6,7,8,9]
# l1=l.append('10')
# for var in l:
#     print(var**2)

# type 2 _2b
# l=[]
# for i in range(2,11,1):
#     j=i**2
#     l.append(j)
#
# print(l)

#wap to remove duplicates --pgm3

# l=[1,2,3,3,4,4,5]
# for i in l:
#     print(i)

# l = [1, 2, 3, 3, 4, 4, 5]
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)
#
# print(l1)

# print the repeated numbers --pgm4
# l = [1, 2, 3, 3, 4, 4, 5]
# l1 = []
# l2=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         l2.append(i)
#
# print(l1)
# print(l2)

# highest number --pgm5-a

# l=[10,20,30,40,10,20]
# print(max(l))

# pgm5_b
l = [10, 20, 30, 40, 10, 20]
l1 = []
max_val = 0
for i in l:
    if i > max_val:
        max_val = i
        l1.append(i)
        l1.append(max_val)

print(l1)
