class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        ...

    def create_driver(self, driver_name):
        ...

    def create_race(self, race_name):
        ...

    def add_car_to_driver(self, driver_name, car_type):
        ...

    def add_driver_to_race(self, race_name, driver_name):
        ...

    def start_race(self, race_name):
        ...
