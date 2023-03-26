from project.truck_driver import TruckDriver
import unittest


class TruckDriverTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('John', 12.0)

    def test_init_name(self):
        self.assertEqual(self.driver.name, 'John')

    def test_init_money(self):
        self.assertEqual(self.driver.money_per_mile, 12.0)

    def test_init_available_cargos(self):
        self.assertEqual(self.driver.available_cargos, {})

    def test_init_available_cargos_with_info(self):
        self.driver.add_cargo_offer('Sozopol', 500)
        self.assertEqual(self.driver.available_cargos, {'Sozopol': 500})

    def test_init_earned_money(self):
        self.assertEqual(self.driver.earned_money, 0)

    def test_valid_earned_money(self):
        self.driver.earned_money = 1000
        self.assertEqual(self.driver.earned_money, 1000)

    def test_invalid_earned_money(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1000
        self.assertEqual(str(ve.exception), "John went bankrupt.")

    def test_add_valid_cargo_offer(self):
        self.assertEqual(self.driver.add_cargo_offer('Sozopol', 500), "Cargo for 500 to Sozopol was added as an offer.")

    def test_add_invalid_cargo_offer(self):
        self.driver.available_cargos = {
            "Sozopol": 500
        }
        with self.assertRaises(Exception) as e:
            self.driver.add_cargo_offer('Sozopol', 500)
        self.assertEqual(str(e.exception), "Cargo offer is already added.")

    def test_valid_drive_best_cargo_offer(self):
        self.driver.available_cargos = {
            "Sozopol": 500,
            "Sofia": 501,
        }
        self.assertEqual(self.driver.drive_best_cargo_offer(), "John is driving 501 to Sofia.")
        self.assertEqual(self.driver.earned_money, 5972)
        self.assertEqual(self.driver.miles, 501)

    def test_invalid_drive_best_cargo_offer(self):
        self.assertEqual(self.driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_best_cargo_offer_earned_money(self):
        self.driver.available_cargos = {
            "Sozopol": 500,
            "Sofia": 501,
        }
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 5972)

    def test_best_cargo_offer_too_many_miles(self):
        bankrupt_driver = TruckDriver('John', 0.01)
        bankrupt_driver.available_cargos = {
            "Sozopol": 10000,
            "Sofia": 501,
        }
        with self.assertRaises(ValueError) as ve:
            bankrupt_driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), "John went bankrupt.")

    def test_best_cargo_offer_same_mileage(self):
        bankrupt_driver = TruckDriver('John', 0.01)
        bankrupt_driver.available_cargos = {
            "Sozopol": 500,
            "Sofia": 500,
        }
        bankrupt_driver.drive_best_cargo_offer()
        self.assertEqual(bankrupt_driver.drive_best_cargo_offer(), "John is driving 500 to Sofia.")

    def test_check_activities(self):
        self.driver.earned_money = 20000
        self.driver.check_for_activities(10000)
        self.assertEqual(self.driver.earned_money, 8250)

    def test_check_activities_bankrupt(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.check_for_activities(10000)
        self.assertEqual(str(ve.exception), "John went bankrupt.")

    def test_eat_valid(self):
        self.driver.earned_money = 1000
        self.driver.eat(500)
        self.assertEqual(self.driver.earned_money, 980)

    def test_sleep_valid(self):
        self.driver.earned_money = 1000
        self.driver.sleep(1000)
        self.assertEqual(self.driver.earned_money, 955)

    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(3000)
        self.assertEqual(self.driver.earned_money, 500)

    def test_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 2500)

    def test_repr(self):
        self.assertEqual(repr(self.driver), "John has 0 miles behind his back.")


if __name__ == '__main__':
    unittest.main()
