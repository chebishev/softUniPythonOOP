from project.car.car import Car


class MuscleCar(Car):
    MINIMUM_SPEED_LIMIT = 250
    MAXIMUM_SPEED_LIMIT = 450

    def max_speed_limit(self):
        return self.MAXIMUM_SPEED_LIMIT

    def min_speed_limit(self):
        return self.MINIMUM_SPEED_LIMIT
