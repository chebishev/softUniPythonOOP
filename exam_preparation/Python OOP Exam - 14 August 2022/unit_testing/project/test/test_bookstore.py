from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(5)

    def test_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 5)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_books_limit_zero_or_bellow(self):
        with self.assertRaises(ValueError) as ve:
            bookstore = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test__len__method(self):
        self.bookstore.receive_book("Python OOP Exam - 14 August 2022", 3)
        self.assertEqual(len(self.bookstore), 3)
        self.bookstore.receive_book("Python OOP Exam - 19 August 2022", 1)
        self.bookstore.receive_book("Python OOP Exam - 19 August 2022", 1)
        self.assertEqual(len(self.bookstore), 5)

    def test_receive_valid_book(self):
        self.assertEqual(self.bookstore.receive_book("Python OOP Exam - 14 August 2022", 3),
                         "3 copies of Python OOP Exam - 14 August 2022 are available in the bookstore.")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {
            "Python OOP Exam - 14 August 2022": 3,
        })

    def test_receive_existing_book(self):
        self.bookstore.receive_book("Python 2022", 3)
        self.assertEqual(self.bookstore.receive_book("Python 2022", 2),
                         "5 copies of Python 2022 are available in the bookstore.")

    def test_receive_too_many_books(self):
        self.bookstore.receive_book("Python OOP Exam - 14 August 2022", 3)
        with self.assertRaises(Exception) as ve:
            self.bookstore.receive_book("Python OOP Exam - 22 August 2022", 5)
        self.assertEqual(str(ve.exception), "Books limit is reached. Cannot receive more books!")

    def test_sell_book_missing_book(self):
        self.bookstore.receive_book("Python OOP Exam - 14 August 2022", 3)
        self.bookstore.receive_book("Python OOP Exam - 19 August 2022", 2)
        self.bookstore.sell_book("Python OOP Exam - 19 August 2022", 1)
        with self.assertRaises(Exception) as e:
            self.bookstore.sell_book("Python OOP Exam - 22 August 2022", 1)
        self.assertEqual(str(e.exception), "Book Python OOP Exam - 22 August 2022 doesn't exist!")

    def test_sell_book_not_enough_copies(self):
        bookstore = Bookstore(5)
        bookstore.receive_book("Python 19 August 2022", 3)
        bookstore.receive_book("Python 14 August 2022", 2)
        bookstore.sell_book("Python 19 August 2022", 1)
        with self.assertRaises(Exception) as e:
            bookstore.sell_book("Python 19 August 2022", 4)
        self.assertEqual(str(e.exception), "Python 19 August 2022 has not enough copies to sell. Left: 2")

    def test_sell_book_valid(self):
        self.bookstore.receive_book("Python 2022", 3)
        self.bookstore.receive_book("Python 2023", 2)
        self.assertEqual(self.bookstore.sell_book("Python 2022", 2), "Sold 2 copies of Python 2022")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {
            "Python 2022": 1,
            "Python 2023": 2,
        })
        self.assertEqual(self.bookstore.total_sold_books, 2)
        self.assertEqual(len(self.bookstore), 3)

    def test__str__returns_correct_message(self):
        self.bookstore.receive_book("Python OOP Exam - 14 August 2022", 3)
        self.bookstore.sell_book("Python OOP Exam - 14 August 2022", 1)
        self.assertEqual(str(self.bookstore),
                         "Total sold books: 1\n"
                         "Current availability: 2\n"
                         " - Python OOP Exam - 14 August 2022: 2 copies")


if __name__ == "__main__":
    main()
