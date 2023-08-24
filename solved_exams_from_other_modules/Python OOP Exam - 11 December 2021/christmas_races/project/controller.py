from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_VALID_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }
    CAR_MODELS = []
    DRIVER_NAMES = []
    RACE_NAMES = []

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if model in self.CAR_MODELS:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.CAR_VALID_TYPES:
            car = self.CAR_VALID_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            self.CAR_MODELS.append(model)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if driver_name in self.DRIVER_NAMES:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        self.DRIVER_NAMES.append(driver_name)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if race_name in self.RACE_NAMES:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        self.RACE_NAMES.append(race_name)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        if driver_name not in self.DRIVER_NAMES:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][0]

        if car_type not in self.CAR_VALID_TYPES:
            raise Exception(f"Car {car_type} could not be found!")

        if not [c for c in self.cars if c.__class__.__name__ == car_type]:
            raise Exception(f"Car {car_type} could not be found!")

        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                if driver.car is None:
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} chose the car {car.model}."
                else:
                    driver_old_car = driver.car.model
                    driver.car.is_taken = False
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver.name} changed his car from {driver_old_car} to {car.model}."
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name, driver_name):
        if race_name not in self.RACE_NAMES:
            raise Exception(f"Race {race_name} could not be found!")

        if driver_name not in self.DRIVER_NAMES:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][0]
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race = [r for r in self.races if r.name == race_name][0]
        if driver_name in race.drivers_names:
            return f"Driver {driver_name} is already added in {race.name} race."

        race.drivers_names.append(driver_name)
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        if race_name not in self.RACE_NAMES:
            raise Exception(f"Race {race_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda d: -d.car.speed_limit)
        output = []
        for index in range(3):
            current_driver = sorted_drivers[index]
            current_driver.number_of_wins += 1
            output.append(f"Driver {current_driver.name} wins the {race_name} "
                          f"race with a speed of {current_driver.car.speed_limit}.")
        return "\n".join(output)

