from project.animal import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE = 60

    def __init__(self, name, age, gender, money_for_care):
        super().__init__(name, gender, age, money_for_care)
        self.money_for_care = Cheetah.MONEY_FOR_CARE
