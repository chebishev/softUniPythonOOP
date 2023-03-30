from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140

    @staticmethod
    def maximum_speed():
        return Thoroughbred.MAXIMUM_SPEED

    def train(self):
        self.speed += 3
