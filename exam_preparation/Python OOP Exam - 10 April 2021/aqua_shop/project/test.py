from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish

controller = Controller()
controller.add_decoration("Plant")
controller.add_decoration("Ornament")
fish_one = FreshwaterFish("Gergana", "Betta splendens", 5)
fish_two = FreshwaterFish("Vladiimir", "Riba 2", 5)
aquarium = FreshwaterAquarium("Freshwater Aquarium")
aquarium.add_fish(fish_one)
aquarium.add_fish(fish_two)
controller.aquariums.append(aquarium)
print(len(controller.decorations_repository.decorations))
controller.insert_decoration("Freshwater Aquarium", "Plant")
print(controller.insert_decoration("Freshwater Aquarium", "Ornament"))

