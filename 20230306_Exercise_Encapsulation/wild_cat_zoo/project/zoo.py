class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
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
        return self.check_budget("workers")

    def tend_animals(self):
        return self.check_budget("animals")

    def check_budget(self, key, needed_budget=None):

        needed_money = {
            "workers": lambda x: sum(x.salary for x in self.workers),
            "animals": lambda x: sum(x.money_for_care for x in self.animals)
        }

        output = {
            "workers": {
                True: "payed your workers",
                False: "pay your workers"
            },
            "animals": {
                True: "tended all the animals",
                False: "tend the animals"
            }
        }

        needed_budget = needed_money[key](needed_budget)

        if needed_budget <= self.__budget:
            self.__budget -= needed_budget
            return f"You {output[key][True]}. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to {output[key][False]}. They are unhappy{'.' if key == 'animals' else ''}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = {
            "Lion": [],
            "Tiger": [],
            "Cheetah": []
        }
        for animal in self.animals:
            animals[animal.__class__.__name__].append(animal.__repr__())

        output = []
        for key, value in animals.items():
            output.append(f"----- {len(animals[key])} {key}s:")
            output.extend(value)

        return f"You have {len(self.animals)} animals\n" + \
            '\n'.join(output)

    def workers_status(self):
        workers = {
            "Keeper": [],
            "Caretaker": [],
            "Vet": []
        }
        for worker in self.workers:
            workers[worker.__class__.__name__].append(worker.__repr__())

        output = []
        for key, value in workers.items():
            output.append(f"----- {len(workers[key])} {key}s:")
            output.extend(value)

        return f"You have {len(self.workers)} workers\n" + \
            '\n'.join(output)
