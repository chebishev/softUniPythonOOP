class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.__page = 0

    def turn_page(self, page):
        current_page = self.__page
        self.__page = page if not 0 <= page <= self.pages else current_page

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.__page}/{self.pages})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return f"{book.title} by {book.author} added to the library."

    def find_book(self, title):
        book = [book for book in self.books if book.title == title][0]

        return book


book = Book("War and Peace", "Leo Tolstoy", 1200)
book_2 = Book("The Catcher in the Rye", "JD Salinger", 500)
library = Library()
print(library.add_book(book))
print(library.add_book(book_2))
library.find_book("War and Peace")
print(library.find_book("The Catcher in the Rye"))
book.turn_page(100)
print(book)
print(book_2)