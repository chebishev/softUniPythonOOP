from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_property(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_existing_worker(self):
        self.plantation.hire_worker("Alice")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Alice")
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_new_work(self):
        self.assertEqual("Alice successfully hired.", self.plantation.hire_worker("Alice"))
        self.assertEqual(self.plantation.workers, ["Alice"])

    def test_len(self):
        self.plantation.hire_worker("Alice")
        self.plantation.hire_worker("Bob")
        self.plantation.planting("Alice", "Apple")
        self.plantation.planting("Bob", "Lemon")
        self.plantation.planting("Alice", "Lime")
        self.assertEqual(3, len(self.plantation))

    def test_planting_missing_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Alice", "Apple")
        self.assertEqual(str(ve.exception), "Worker with name Alice is not hired!")

    def test_planting_existing_worker_not_in_dictionary(self):
        self.plantation.hire_worker("Alice")
        self.assertEqual(self.plantation.planting("Alice", "Apple"), "Alice planted it's first Apple.")
        self.assertEqual(self.plantation.plants, {"Alice": ["Apple"]})
        self.assertEqual(len(self.plantation), 1)

    def test_planting_existing_worker_in_dictionary(self):
        self.plantation.hire_worker("Alice")
        self.plantation.plants = {
            "Alice": ["Apple", "Lemon"],
        }
        self.assertEqual(self.plantation.planting("Alice", "Apple"), "Alice planted Apple.")
        self.assertEqual(self.plantation.plants, {"Alice": ["Apple", "Lemon", "Apple"]})
        self.assertEqual(len(self.plantation), 3)

    def test_full_plantation_planting(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Alice")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Alice", "Apple")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test__str__(self):
        self.plantation.workers = ["Alice", "Bob"]
        self.plantation.planting("Alice", "Apple")
        self.plantation.planting("Bob", "Lemon")
        self.plantation.planting("Alice", "Lime")
        self.assertEqual(str(self.plantation),
                         "Plantation size: 10\n"
                         "Alice, Bob\n"
                         "Alice planted: Apple, Lime\n"
                         "Bob planted: Lemon")

    def test__repr__(self):
        self.plantation.workers = ["Alice", "Bob"]
        self.assertEqual(self.plantation.__repr__(), "Size: 10\n"
                         "Workers: Alice, Bob")


if __name__ == '__main__':
    main()
