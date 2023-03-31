from project.movie_specification.movie import Movie


class Fantasy(Movie):
    MINIMUM_AGE = 6

    def __init__(self, title, year, owner, age_restriction=MINIMUM_AGE):
        super().__init__(title, year, owner, age_restriction)

    @property
    def minimum_age(self):
        return Fantasy.MINIMUM_AGE
