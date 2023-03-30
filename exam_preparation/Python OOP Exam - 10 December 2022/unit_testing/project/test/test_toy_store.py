from horse_racings.project import ToyStore
import unittest


class ToyStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_valid_add_toy(self):
        shelf = "D"
        toy_name = "Fancy Toy"
        self.assertEqual(self.toy_store.add_toy(shelf, toy_name), "Toy:Fancy Toy placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf[shelf], toy_name)

    def test_invalid_shelf(self):
        shelf = "H"
        toy_name = "Fancy Toy"
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_toy_exists(self):
        self.toy_store.toy_shelf = {
            "A": "Test_toy",
        }
        with self.assertRaises(Exception) as e:
            self.toy_store.add_toy("A", "Test_toy")
        self.assertEqual(str(e.exception), "Toy is already in shelf!")

    def test_taken_shelf(self):
        self.toy_store.toy_shelf = {
            "A": "Test_toy",
        }
        with self.assertRaises(Exception) as e:
            self.toy_store.add_toy("A", "new_toy")
        self.assertEqual(str(e.exception), "Shelf is already taken!")

    def test_valid_remove_toy(self):
        self.toy_store.toy_shelf = {
            "A": "Test_toy",
        }
        shelf = "A"
        toy_name = "Test_toy"
        self.assertEqual(self.toy_store.remove_toy(shelf, toy_name), f"Remove toy:{toy_name} successfully!")
        self.assertEqual(self.toy_store.toy_shelf[shelf], None)

    def test_shelf_exists(self):
        with self.assertRaises(Exception) as e:
            self.toy_store.remove_toy("K", "Test_toy")
        self.assertEqual(str(e.exception), "Shelf doesn't exist!")

    def test_toy_exists(self):
        self.toy_store.toy_shelf = {
            "A": "Test_toy",
        }
        with self.assertRaises(Exception) as e:
            self.toy_store.remove_toy("A", "wrong_toy")
        self.assertEqual(str(e.exception), "Toy in that shelf doesn't exists!")

