from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("My train", 10)

    def test_init(self):
        self.assertEqual("My train", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_no_capacity(self):
        self.train.capacity = 0
        with self.assertRaises(ValueError) as ve:
            self.train.add("Pesho")
        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual([], self.train.passengers)

    def test_add_existing_passenger(self):
        self.train.passengers = ["Pesho", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Pesho")
        self.assertEqual("Passenger Pesho Exists", str(ve.exception))
        self.assertEqual(["Pesho", "Gosho"], self.train.passengers)

    def test_add_valid(self):
        self.assertEqual(self.train.add("Pesho"), "Added passenger Pesho")
        self.assertEqual(["Pesho"], self.train.passengers)

    def test_remove_missing_passenger(self):
        self.train.add("Pesho")
        self.train.add("Gosho")
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Dimo")
        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual(["Pesho", "Gosho"], self.train.passengers)

    def test_remove_valid_passenger(self):
        self.train.add("Pesho")
        self.train.add("Gosho")
        self.assertEqual(self.train.remove("Pesho"), "Removed Pesho")
        self.assertEqual(["Gosho"], self.train.passengers)