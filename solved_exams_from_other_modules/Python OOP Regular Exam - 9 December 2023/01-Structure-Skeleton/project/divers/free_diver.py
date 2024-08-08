from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN = 120
    REDUCE_PERCENT = 0.60

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)
