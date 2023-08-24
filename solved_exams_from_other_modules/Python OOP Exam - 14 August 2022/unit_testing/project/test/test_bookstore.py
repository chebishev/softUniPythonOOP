from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore.total_sold_books, 0)

    def test_books_limit_below_limit(self):
        with self.assertRaises(ValueError) as ve:
            bookstore = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test__len__(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 2, "Barry Hotter": 3}
        self.assertEqual(len(self.bookstore), 5)

    def test_receive_book_out_of_limit(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 5, "Rohan": 5}
        with self.assertRaises(Exception) as e:
            self.bookstore.receive_book("Mystery Book", 2)
        self.assertEqual(str(e.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_not_existing(self):
        self.assertEqual(self.bookstore.receive_book("Lord of the Rings", 2),
                         "2 copies of Lord of the Rings are available in the bookstore.")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles,
                         {"Lord of the Rings": 2})

    def test_receive_book_existing(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 2}
        self.assertEqual(self.bookstore.receive_book("Harry Potter", 2),
                         "4 copies of Harry Potter are available in the bookstore.")

    def test_sell_not_existing_book(self):
        with self.assertRaises(Exception) as e:
            self.bookstore.sell_book("Harry Potter", 2)
        self.assertEqual(str(e.exception), "Book Harry Potter doesn't exist!")

    def test_sell_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 2}
        with self.assertRaises(Exception) as e:
            self.bookstore.sell_book("Harry Potter", 3)
        self.assertEqual(str(e.exception),
                         "Harry Potter has not enough copies to sell. Left: 2")

    def test_sell_book_valid(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 2}
        self.assertEqual(self.bookstore.sell_book("Harry Potter", 2), "Sold 2 copies of Harry Potter")
        self.assertEqual(self.bookstore.total_sold_books, 2)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"Harry Potter": 0})

    def test__str__(self):
        self.bookstore.receive_book("Harry Potter", 5)
        self.bookstore.receive_book("Rohan", 5)
        self.bookstore.sell_book("Harry Potter", 2)
        self.bookstore.sell_book("Rohan", 2)
        self.assertEqual(str(self.bookstore), "Total sold books: 4\n"
                                              "Current availability: 6\n"
                                              " - Harry Potter: 3 copies\n"
                                              " - Rohan: 3 copies")


if __name__ == "__main__":
    main()
