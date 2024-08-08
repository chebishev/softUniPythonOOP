from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):

    def __init__(self, name: str, points: float):
        super().__init__(name, points, 180)
        self.name = name
        self.points = points



# 5 + 9.1 + 8.5 = 22.6
# 540 - 90 - 180 - 180 - 90 = 0