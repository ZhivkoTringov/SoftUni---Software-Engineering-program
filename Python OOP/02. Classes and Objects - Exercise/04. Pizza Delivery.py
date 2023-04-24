class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        elif ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_quantity
        elif ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        elif ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

    def make_order(self):
        self.ordered = True
        result = ', '.join([f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {result} and the price will be {self.price}lv."