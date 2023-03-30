from project.movie_specification.movie import Movie


class Action(Movie):
    MINIMUM_AGE = 12

    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @staticmethod
    def movie_genre():
        return "Action"

    @staticmethod
    def minimum_age():
        return Action.MINIMUM_AGE
