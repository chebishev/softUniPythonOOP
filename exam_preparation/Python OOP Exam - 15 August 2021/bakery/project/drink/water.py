from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.get_price, brand)

    @property
    def get_price(self):
        return 1.50
