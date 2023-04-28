from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        ...

    def add_decoration(self, decoration_type):
        ...

    def insert_decoration(self, aquarium_name, decoration_type):
        ...

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        ...

    def feed_fish(self, aquarium_name):
        ...

    def calculate_value(self, aquarium_name):
        ...

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return "\n".join(result)