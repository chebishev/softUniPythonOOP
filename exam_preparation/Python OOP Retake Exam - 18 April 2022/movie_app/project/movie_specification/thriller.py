from project.movie_specification.movie import Movie


class Thriller(Movie):
    MINIMUM_AGE = 16

    def __init__(self, title, year, owner, age_restriction=MINIMUM_AGE):
        super().__init__(title, year, owner, age_restriction)

    @property
    def minimum_age(self):
        return Thriller.MINIMUM_AGE
