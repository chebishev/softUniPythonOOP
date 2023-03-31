from project.movie_specification.movie import Movie


class Action(Movie):
    MINIMUM_AGE = 12

    def __init__(self, title, year, owner, age_restriction=MINIMUM_AGE):
        super().__init__(title, year, owner, age_restriction)

    @property
    def minimum_age(self):
        return Action.MINIMUM_AGE
