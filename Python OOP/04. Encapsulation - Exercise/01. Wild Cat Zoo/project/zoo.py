class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if self.__budget < total_salary:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_tending = 0
        for animal in self.animals:
            total_tending += animal.money_for_care
        if self.__budget >= total_tending:
            self.__budget -= total_tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__animal_str('Lion')
        result += self.__animal_str('Tiger')
        result += self.__animal_str('Cheetah')
        return result.strip()

    def __animal_str(self, animal_type):
        diff_type = []
        for animal in self.animals:
            if animal.__class__.__name__ == animal_type:
                diff_type.append(animal)
        result = f'----- {len(diff_type)} {animal_type}s:\n'
        for animal_type in diff_type:
            result += repr(animal_type) + '\n'
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__workers_str('Keeper')
        result += self.__workers_str('Caretaker')
        result += self.__workers_str('Vet')
        return result.strip()

    def __workers_str(self, worker_type):
        diff_type = []
        for worker in self.workers:
            if worker.__class__.__name__ == worker_type:
                diff_type.append(worker)
        result = f'----- {len(diff_type)} {worker_type}s:\n'
        for worker_type in diff_type:
            result += repr(worker_type) + '\n'
        return result