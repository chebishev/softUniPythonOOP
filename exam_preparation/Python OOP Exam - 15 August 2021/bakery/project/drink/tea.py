from project.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.50

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.PRICE, brand)
