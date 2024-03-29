class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) >= self.__capacity:
            return 'not enough room in the inventory'
        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __get_items_count(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"