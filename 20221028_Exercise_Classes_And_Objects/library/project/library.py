from user import User


class Library:
    def __init__(self):
        self.user_records = []
        # {author: [books]}
        self.books_available = {}
        # {usernames: {book names: days to return}}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name not in self.books_available[author]:
            return f"The book \"{book_name}\" is already rented and will be available in " \
                   f"{self.rented_books[user.username][book_name]} days!"

        user.books.append(book_name)
        self.rented_books[user.username] = {book_name: days_to_return}
        self.books_available[author].remove(book_name)
        self.user_records.append(user.__str__())  # currently don't know what to do with this attribute

        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        del self.rented_books[user.username][book_name]
        self.books_available[author].append(book_name)
