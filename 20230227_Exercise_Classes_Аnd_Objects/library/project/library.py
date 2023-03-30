from horse_racings.project import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name not in self.books_available[author]:
            return f"The book \"{book_name}\" is already rented and will be available in " \
                   f"{self.rented_books[user.username][book_name]} days!"

        self.books_available[author].remove(book_name)
        if user.username not in self.rented_books:
            self.rented_books[user.username] = {}
        self.rented_books[user.username][book_name] = days_to_return
        user.books.append(book_name)

        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)
        del self.rented_books[user.username][book_name]
        self.books_available[author].append(book_name)
