def f1():
    yield 5
    yield 6
a=f1()
print(a)

for i in a:
    print(i)