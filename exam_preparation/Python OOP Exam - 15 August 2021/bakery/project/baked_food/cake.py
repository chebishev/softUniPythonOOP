from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):

    def __init__(self, name, price):
        super().__init__(name, self.get_portion, price)

    @property
    def get_portion(self):
        return 245
