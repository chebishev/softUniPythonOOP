from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREASE = 2

    def __init__(self, name, species, price, size=5):
        super().__init__(name, species, size, price)
