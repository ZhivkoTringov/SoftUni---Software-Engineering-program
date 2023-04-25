from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

# f = Fruit('banana', '22.02.2021')
# print(f.name)
# print(f.expiration_date)
