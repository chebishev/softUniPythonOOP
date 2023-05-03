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
for decoration in controller.decorations_repository.decorations:
    print(decoration.__class__.__name__)
print(controller.insert_decoration("Freshwater Aquarium", "Plant"))
print(str(aquarium))
for decoration in controller.decorations_repository.decorations:
    print(decoration.__class__.__name__)
print(controller.insert_decoration("Freshwater Aquarium", "Ornament"))
controller.add_decoration("Plant")
controller.add_decoration("Ornament")
print(controller.report())
print(controller.decorations_repository.remove(Plant()))
print(controller.report())
