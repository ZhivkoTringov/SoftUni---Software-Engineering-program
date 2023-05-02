from abc import ABC, abstractmethod


class Vehicle(ABC):
    AiR_CONDITION = None

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        needed_liters = (self.fuel_consumption + Car.AIR_CONDITION) * distance
        if needed_liters <= self.fuel_quantity:
            self.fuel_quantity -= needed_liters
            return self.fuel_quantity
        return self.fuel_quantity


class Truck(Vehicle):
    AIR_CONDITION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)

    def drive(self, distance):
        needed_liters = (self.fuel_consumption + Truck.AIR_CONDITION) * distance
        if needed_liters <= self.fuel_quantity:
            self.fuel_quantity -= needed_liters
            return self.fuel_quantity