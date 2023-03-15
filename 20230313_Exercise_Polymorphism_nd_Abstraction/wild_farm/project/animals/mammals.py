from project.animals.animal import Mammal


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def weight_gain(self):
        return 0.10

    @property
    def food_check(self):
        return ["Vegetable", "Fruit"]


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def weight_gain(self):
        return 0.40

    @property
    def food_check(self):
        return ["Meat"]


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def weight_gain(self):
        return 0.30

    @property
    def food_check(self):
        return ["Meat", "Vegetable"]


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def weight_gain(self):
        return 1.00

    @property
    def food_check(self):
        return ["Meat"]
