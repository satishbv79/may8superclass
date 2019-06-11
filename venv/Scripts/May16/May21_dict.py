#pgm1
d={'a':1,'b':2,'c':3}
# print(type(d))
# print(d.get('b'))
# print(d[0])
#
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

#pgm2
d={'a':1,'b':2,'c':3}
print(len(d))

#print(d['a']) #prints corresponding key value pair
#del(d['a']) # removes corresponding key value pair

d.popitem() # remove lastkey value pairs
#d.pop('a')

for i in d.items():
    print(i)