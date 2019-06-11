class flight:
    def __init__(self):
        self.meals='Idli'
        print(self.meals)

class flight1(flight):
    def __init__(self):
        super().__init__()
        self.meals='vada'
        print(self.meals)

f1=flight1() #idli vada
f2=flight()

