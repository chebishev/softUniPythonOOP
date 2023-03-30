from project.movie_specification.movie import Movie


class Fantasy(Movie):
    MINIMUM_AGE = 6

    def __init__(self, title, year, owner, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @staticmethod
    def movie_genre():
        return "Fantasy"

    @staticmethod
    def minimum_age():
        return Fantasy.MINIMUM_AGE
