from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    def __init__(self, name, kind, price, weight=9):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += 3
