from horse_racings.project import Animal


class Tiger(Animal):
    MONEY_FOR_CARE = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.MONEY_FOR_CARE)

