from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class Controller:
    VALID_AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }
    VALID_DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in self.VALID_AQUARIUM_TYPES:
            return "Invalid aquarium type."
        self.aquariums.append(self.VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in self.VALID_DECORATION_TYPES:
            return "Invalid decoration type."

        self.decorations_repository.add(self.VALID_DECORATION_TYPES[decoration_type])
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        try:
            decoration = [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type][0]
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium.append(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

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