from project.animals.animal import Bird
from project.food import Fruit, Seed, Meat, Vegetable


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_wight(self):
        return 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

    @property
    def food_that_eats(self):
        return [Vegetable, Meat, Seed, Fruit]

    @property
    def gained_wight(self):
        return 0.35
