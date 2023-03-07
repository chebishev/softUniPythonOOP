from project.animal import Animal
from project.tiger import Tiger


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
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
        pass
    # "You have no budget to pay your workers. They are unhappy"
    # "You payed your workers. They are happy. Budget left: {left_budget}"

    def tend_animals(self):
        pass
    # "You have no budget to tend the animals. They are unhappy."
    # "You tended all the animals. They are happy. Budget left: {left_budget}"
