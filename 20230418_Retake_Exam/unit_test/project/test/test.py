from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("1", "Military", 100, 10)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, "1")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 10)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            Robot("2", "", 100, 10)
        self.assertEqual(str(ve.exception),
                         f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'")

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_existing_component(self):
        self.robot.hardware_upgrades = ["Battery", "Memory"]
        self.assertEqual(self.robot.upgrade("Battery", 2), "Robot 1 was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades, ["Battery", "Memory"])

    def test_valid_upgrade(self):
        self.assertEqual(self.robot.upgrade("Battery", 2),
                         "Robot 1 was upgraded with Battery.")
        self.assertEqual(self.robot.hardware_upgrades, ["Battery"])
        self.assertEqual(self.robot.price, 13)

    def test_update_existing_version(self):
        self.robot.software_updates = [1, 2, 3]
        self.assertEqual(self.robot.update(1, 2), "Robot 1 was not updated.")
        self.assertEqual(self.robot.software_updates, [1, 2, 3])
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.update(5, 110), "Robot 1 was not updated.")
        self.assertEqual(self.robot.software_updates, [1, 2, 3])
        self.assertEqual(self.robot.available_capacity, 100)

    def test_valid_update(self):
        self.assertEqual(self.robot.update(1, 2), "Robot 1 was updated to version 1.")
        self.assertEqual(self.robot.software_updates, [1])
        self.assertEqual(self.robot.available_capacity, 98)

    def test__gt__valid(self):
        robot1 = Robot("2", "Education", 100, 9)
        self.assertEqual(self.robot > robot1,
                         "Robot with ID 1 is more expensive than Robot with ID 2.")

    def test__gt__equal(self):
        robot1 = Robot("2", "Education", 100, 10)
        self.assertEqual(self.robot > robot1, "Robot with ID 1 costs equal to Robot with ID 2.")

    def test__gt__less(self):
        robot1 = Robot("2", "Education", 100, 11)
        self.assertEqual(self.robot > robot1, "Robot with ID 1 is cheaper than Robot with ID 2.")