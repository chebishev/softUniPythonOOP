from project.car.car import Car


class SportsCar(Car):
    MINIMUM_SPEED_LIMIT = 400
    MAXIMUM_SPEED_LIMIT = 600

    def max_speed_limit(self):
        return self.MAXIMUM_SPEED_LIMIT

    def min_speed_limit(self):
        return self.MINIMUM_SPEED_LIMIT
