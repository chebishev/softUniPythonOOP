from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    STRENGTH_CLIMB_LIMIT = 75

    def __init__(self, name: str):
        super().__init__(name, 150)
        self.name = name

    def climb(self, peak: object):
        if peak.difficulty_level == "Advanced":
            index = 1.3
        else:
            index = 2.5
        self.strength -= (30 * index)
        self.conquered_peaks.append(peak.name)
