from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }
    VALID_DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant
    }
    POSSIBLE_FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
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

        self.decorations_repository.add(self.VALID_DECORATION_TYPES[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None" or decoration_type not in self.VALID_DECORATION_TYPES:
            return f"There isn't a decoration of type {decoration_type}."

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self.POSSIBLE_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        fish = self.POSSIBLE_FISH_TYPES[fish_type](fish_name, fish_species, price)
        aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
        aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        total = 0
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for fish in aquarium.fish:
                    total += fish.price
                for decoration in aquarium.decorations:
                    total += decoration.price

        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return "\n".join(result)
