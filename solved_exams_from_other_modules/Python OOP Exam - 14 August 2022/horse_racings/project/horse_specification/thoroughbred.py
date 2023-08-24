from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    TRAIN_SPEED = 3

    @staticmethod
    def maximum_speed():
        return Thoroughbred.MAXIMUM_SPEED

    @staticmethod
    def train_speed():
        return Thoroughbred.TRAIN_SPEED
