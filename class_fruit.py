class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass
smith = Apple("green","tart")
carelian = Grape("purple","sweet")
print(smith.flavor)
print(carelian.color)
