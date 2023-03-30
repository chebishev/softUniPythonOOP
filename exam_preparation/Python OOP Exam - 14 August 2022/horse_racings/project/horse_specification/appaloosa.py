from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120

    @staticmethod
    def maximum_speed():
        return Appaloosa.MAXIMUM_SPEED

    def train(self):
        self.speed += 2
