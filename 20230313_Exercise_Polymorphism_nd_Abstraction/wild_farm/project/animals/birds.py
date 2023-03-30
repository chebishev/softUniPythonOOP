from horse_racings.project import Bird


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def weight_gain(self):
        return 0.25

    @property
    def food_check(self):
        return ["Meat"]


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def weight_gain(self):
        return 0.35

    @property
    def food_check(self):
        return ["Meat", "Vegetable", "Fruit", "Seed"]
