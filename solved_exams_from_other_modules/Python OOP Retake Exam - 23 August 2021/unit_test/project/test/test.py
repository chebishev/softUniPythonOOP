from project.library import Library
from unittest import TestCase, main

class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Test")

    def test_init(self):
        self.assertEqual(self.library.name, "Test")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            library = Library("")
        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book_new(self):
        self.library.add_book("Test", "Test")
        self.assertEqual(self.library.books_by_authors, {"Test": ["Test"]})

    def test_add_book_existing(self):
        self.library.add_book("Test", "Test")
        self.library.add_book("Fest", "Test")
        self.library.add_book("Test", "Fest")
        self.assertEqual(self.library.books_by_authors, {"Test": ["Test", "Fest"], "Fest": ["Test"]})

    def test_add_reader_new(self):
        self.library.add_reader("Test")
        self.assertEqual(self.library.readers, {"Test": []})

    def test_add_reader_existing(self):
        self.library.add_reader("Test")
        self.assertEqual(self.library.add_reader("Test"), "Test is already registered in the Test library.")
        self.assertEqual(self.library.readers, {"Test": []})

    def test_rent_book_missing_reader(self):
        self.assertEqual(self.library.rent_book("John", "Tolkin", "LOTR"),
                         "John is not registered in the Test Library.")

    def test_rent_book_missing_author(self):
        self.library.add_reader("John")
        self.assertEqual(self.library.rent_book("John", "Tolkin", "LOTR"),
                         f"Test Library does not have any Tolkin's books.")

    def test_rent_book_missing_title(self):
        self.library.add_reader("John")
        self.library.add_book("Tolkin", "LOTR")
        self.assertEqual(self.library.rent_book("John", "Tolkin", "Hobbit"),
                         'Test Library does not have Tolkin\'s "Hobbit".')

    def test_rent_book_valid(self):
        self.library.add_reader("John")
        self.library.add_book("Tolkin", "LOTR")
        self.library.add_book("Tolkin", "Hobbit")
        self.library.rent_book("John", "Tolkin", "LOTR")
        self.assertEqual(self.library.readers, {"John": [{"Tolkin": "LOTR"}]})
        self.assertEqual(self.library.books_by_authors, {"Tolkin": ["Hobbit"]})
