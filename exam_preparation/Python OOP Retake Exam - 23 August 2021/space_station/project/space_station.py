from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_VALID_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }
    MISSIONS = {
        "Successful": 0,
        "Unsuccessful": 0
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.ASTRONAUT_VALID_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.ASTRONAUT_VALID_TYPES[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items.extend(items.split(', '))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = list(
            filter(lambda astronaut: astronaut.oxygen > 30, self.astronaut_repository.astronauts))
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_on_mission = sorted(suitable_astronauts, key=lambda astronaut: astronaut.oxygen, reverse=True)
        if len(suitable_astronauts) > 5:
            astronauts_on_mission = astronauts_on_mission[:5]
        astronauts_on_mission = astronauts_on_mission[::-1]

        astronauts_counter = 0
        while astronauts_on_mission:
            if not planet.items:
                self.MISSIONS["Successful"] += 1
                return f"Planet: {planet.name} was explored. {astronauts_counter} " \
                       f"astronauts participated in collecting items."

            current_astronaut = astronauts_on_mission.pop()
            astronauts_counter += 1
            while planet.items:
                current_item = planet.items.pop()
                current_astronaut.backpack.append(current_item)
                current_astronaut.breathe()
                if current_astronaut.oxygen <= 0:
                    break

        if planet.items:
            self.MISSIONS["Unsuccessful"] += 1
            return "Mission is not completed."

    def report(self):
        result = [f"{self.MISSIONS['Successful']} successful missions!",
                  f"{self.MISSIONS['Unsuccessful']} missions were not completed!", "Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            result.append(f"Backpack items: {', '.join(astronaut.backpack) if astronaut.backpack else 'none'}")
        return '\n'.join(result)
