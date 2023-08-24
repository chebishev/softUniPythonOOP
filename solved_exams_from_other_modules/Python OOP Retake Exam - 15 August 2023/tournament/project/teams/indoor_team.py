from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET = 500.0
    ADVANTAGE = 145

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, self.BUDGET)
