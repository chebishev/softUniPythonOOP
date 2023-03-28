from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 100)

    def test_initialization_values(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_valid_drive_method(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_valid_refuel_method(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 10)

    def test_too_much_fuel_refuel(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(100)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_if__str__returns_correct_message(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 100 horse power with 50 fuel left "
                                            "and 1.25 fuel consumption")


if __name__ == "__main__":
    main()