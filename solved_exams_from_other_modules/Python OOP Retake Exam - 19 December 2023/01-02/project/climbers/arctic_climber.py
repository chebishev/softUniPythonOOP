from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    STRENGTH_CLIMB_LIMIT = 100

    def __init__(self, name: str):
        super().__init__(name, 200)
        self.name = name

    def climb(self, peak: object):
        if peak.difficulty_level == "Extreme":
            self.strength -= (20 * 2)
        else:
            self.strength -= (20 * 1.5)
        self.conquered_peaks.append(peak.name)


