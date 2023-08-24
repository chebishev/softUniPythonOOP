from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE_INCREASE = 3

    def __init__(self, name, species, price, size=3):
        super().__init__(name, species, size, price)
