from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    SUITABLE_WATER = {
        "FreshwaterFish": "FreshwaterAquarium",
        "SaltwaterFish": "SaltwaterAquarium"
    }

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total = 0
        for decoration in self.decorations:
            total += decoration.comfort
        return total

    def add_fish(self, fish):

        if self.capacity <= len(self.fish):
            return "Not enough capacity."

        fish_type = fish.__class__.__name__

        if not self.SUITABLE_WATER[fish_type] == self.__class__.__name__:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = " ".join(fish.name for fish in self.fish) if self.fish else "none"

        return f"{self.name}:\n" \
               f"Fish: {fish_names}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
