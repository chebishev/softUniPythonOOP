from project.movie_specification.movie import Movie


class Thriller(Movie):
    MINIMUM_AGE = 16

    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @staticmethod
    def movie_genre():
        return "Thriller"

    @staticmethod
    def minimum_age():
        return Thriller.MINIMUM_AGE
