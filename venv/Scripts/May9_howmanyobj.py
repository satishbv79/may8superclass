class a:
    count = 0;

    def __init__(self):
        a.count = a.count + 1

    @classmethod
    def obj_count(cls):
        print("num of obj created", a.count)


a1 = a()
a2 = a()
a3 = a()
a.obj_count()
