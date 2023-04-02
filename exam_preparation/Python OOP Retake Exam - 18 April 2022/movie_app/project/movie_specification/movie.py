from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):
    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.minimum_age:
            raise ValueError(f"{self.movie_genre} movies must be "
                             f"restricted for audience under {self.minimum_age} years!")

        self.__age_restriction = value

    @property
    def movie_genre(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def minimum_age(self):
        ...

    def details(self):
        return f"{self.movie_genre} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
