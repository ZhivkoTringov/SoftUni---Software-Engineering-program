class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, defend):
        self.health -= defend
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            return

    def heal(self, heal):
        self.health += heal