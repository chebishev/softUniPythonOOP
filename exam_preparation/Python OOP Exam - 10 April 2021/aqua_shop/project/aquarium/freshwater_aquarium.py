from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name, capacity=50):
        super().__init__(name, capacity)

# fish_one = FreshwaterFish("Gergana", "Betta splendens", 5)
# fish_two = FreshwaterFish("Vladiimir", "Riba 2", 5)
# aquarium = FreshwaterAquarium("Freshwater Aquarium")
# aquarium.add_fish(fish_one)
# aquarium.add_fish(fish_two)
# aquarium.remove_fish(fish_two)
# print(str(aquarium))