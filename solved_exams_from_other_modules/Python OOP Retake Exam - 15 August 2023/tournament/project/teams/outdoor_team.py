from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1000.0
    ADVANTAGE = 115

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, self.BUDGET)
