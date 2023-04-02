from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def check_movie(self, movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def register_user(self, username, age) -> str:
        try:
            [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            new_user = User(username, age)
            self.users_collection.append(new_user)
            return f"{username} registered successfully."

        raise Exception("User already exists!")

    def upload_movie(self, username, movie) -> str:

        try:
            user = [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if movie.owner.username != user.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs) -> str:
        self.check_movie(movie)

        try:
            user = [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            movie.__setattr__(k, v)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie) -> str:

        self.check_movie(movie)

        try:
            user = [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")
        if movie not in user.movies_owned:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie) -> str:
        try:
            user = [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")

        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie) -> str:
        try:
            user = [x for x in self.users_collection if x.username == username][0]
        except IndexError:
            raise Exception("This user does not exist!")
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        if not sorted_movies:
            return "No movies found."

        return '\n'.join(movie.details() for movie in sorted_movies)

    def __str__(self) -> str:
        all_users = ", ".join(u.username for u in self.users_collection) if self.users_collection else "No users."
        all_movies = ", ".join(m.title for m in self.movies_collection) if self.movies_collection else "No movies."

        return f"All users: {all_users}\nAll movies: {all_movies}"
