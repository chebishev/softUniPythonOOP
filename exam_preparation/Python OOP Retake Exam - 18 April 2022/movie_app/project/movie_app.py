class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.user_collection = []

    def register_user(self, username, age):
        ...

    def upload_movie(self, username, movie):
        ...

    def edit_movie(self, username, movie, **kwargs):
        ...

    def delete_movie(self, username, movie):
        ...

    def like_movie(self, username, movie):
        ...

    def dislike_movie(self, username, movie):
        ...

    def display_movies(self):
        ...

    def __str__(self):
        ...