class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarTests(unittest.TestCase):

    def test_correct_variable_make(self):
        test_car = Car("FORD", "b", 1, 4)
        self.assertEqual(test_car.make, "FORD")

    def test_incorrect_variable_make(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("", "b", 1, 4)
        self.assertEqual(str(e.exception), "Make cannot be null or empty!")

    def test_correct_variable_model(self):
        test_car = Car("FORD", "b", 1, 4)
        self.assertEqual(test_car.model, "b")

    def test_incorrect_variable_model(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("a", "", 1, 4)
        self.assertEqual(str(e.exception), "Model cannot be null or empty!")

    def test_correct_variable_fuel_consumption(self):
        test_car = Car("FORD", "b", 1, 4)
        self.assertEqual(test_car.fuel_consumption, 1)

    def test_incorrect_variable_fuel_consumption(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("FORD", "b", 0, 4)
        self.assertEqual(str(e.exception), "Fuel consumption cannot be zero or negative!")

    def test_correct_variable_fuel_capacity(self):
        test_car = Car("FORD", "b", 1, 4)
        self.assertEqual(test_car.fuel_capacity, 4)

    def test_incorrect_variable_fuel_capacity(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("FORD", "b", 1, 0)
        self.assertEqual(str(e.exception), "Fuel capacity cannot be zero or negative!")

    def test_correct_variable_fuel_amount(self):
        test_car = Car("FORD", "b", 1, 4)
        self.assertEqual(test_car.fuel_amount, 0)

    def test_incorrect_variable_fuel_amount(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("FORD", "b", 1, 4)
            test_car.fuel_amount = -5
        self.assertEqual(str(e.exception), "Fuel amount cannot be negative!")

    def test_valid_refuel(self):
        test_car = Car("FORD", "b", 1, 4)
        test_car.refuel(10)
        self.assertEqual(test_car.fuel_amount, 4)

    def test_invalid_refuel(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("FORD", "b", 1, 4)
            test_car.refuel(-5)
        self.assertEqual(str(e.exception), "Fuel amount cannot be zero or negative!")

    def test_valid_drive(self):
        test_car = Car("FORD", "b", 1, 4)
        test_car.refuel(10)
        test_car.drive(100)
        self.assertEqual(test_car.fuel_amount, 3)

    def test_invalid_drive(self):
        with self.assertRaises(Exception) as e:
            test_car = Car("FORD", "b", 1, 4)
            test_car.drive(5)
        self.assertEqual(str(e.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
