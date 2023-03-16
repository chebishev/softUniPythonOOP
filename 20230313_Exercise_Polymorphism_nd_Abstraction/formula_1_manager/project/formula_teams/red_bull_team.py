from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = {
        "Oracle": {
            1: 1_500_000,
            2: 800_000,
        },
        "Honda": {
            8: 20_000,
            10: 10_000,
        }
    }

    @property
    def sponsors(self):
        return RedBullTeam.SPONSORS

    @staticmethod
    def expenses():
        return 250_000
