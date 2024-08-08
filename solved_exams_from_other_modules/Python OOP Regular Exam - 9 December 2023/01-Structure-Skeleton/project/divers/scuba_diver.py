from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540
    REDUCE_PERCENT = 0.30

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)


