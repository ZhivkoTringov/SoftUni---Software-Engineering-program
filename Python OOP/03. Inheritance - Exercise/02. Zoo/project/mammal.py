from project.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
