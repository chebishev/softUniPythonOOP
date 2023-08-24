from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    TRAIN_SPEED = 2

    @staticmethod
    def maximum_speed():
        return Appaloosa.MAXIMUM_SPEED

    @staticmethod
    def train_speed():
        return Appaloosa.TRAIN_SPEED
