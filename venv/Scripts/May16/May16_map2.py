#case5
l = [1, 2, 3, 4, 5, 6, 7, 8]
from functools import reduce

o1 = filter(lambda x: x < 6, l)
o2 = map(lambda y: y * 2, o1)
o3 = reduce(lambda p, q: p + q, o1)
print((o3))
