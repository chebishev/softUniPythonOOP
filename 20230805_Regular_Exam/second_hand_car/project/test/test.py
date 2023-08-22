from unittest import TestCase

from project.second_hand_car import SecondHandCar


class SecondHandCarTest(TestCase):
    def setUp(self):
        self.car = SecondHandCar('BMW', 'Sedan', 1000, 10000)
        self.car2 = SecondHandCar('BMW', 'Sedan', 1000, 8000)

    def test_init(self):
        self.assertEqual(self.car.model, 'BMW')
        self.assertEqual(self.car.car_type, 'Sedan')
        self.assertEqual(self.car.mileage, 1000)
        self.assertEqual(self.car.price, 10000)
        self.assertEqual(self.car.repairs, [])

    def test_invalid_price_equal(self):
        with self.assertRaises(ValueError) as e:
            car = SecondHandCar('BMW', 'Sedan', 125, 1)
        self.assertEqual(str(e.exception), 'Price should be greater than 1.0!')

    def test_invalid_price_less(self):
        with self.assertRaises(ValueError) as e:
            car = SecondHandCar('BMW', 'Sedan', 125, 0.99)
        self.assertEqual(str(e.exception), 'Price should be greater than 1.0!')

    def test_invalid_mileage_equal(self):
        with self.assertRaises(ValueError) as e:
            car = SecondHandCar('BMW', 'Sedan', 100, 10000)
        self.assertEqual(str(e.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_invalid_mileage_less(self):
        with self.assertRaises(ValueError) as e:
            car = SecondHandCar('BMW', 'Sedan', 99, 10000)
        self.assertEqual(str(e.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_higher(self):
        self.assertEqual(self.car.price, 10000)
        with self.assertRaises(ValueError) as e:
            self.car.set_promotional_price(10001)
        self.assertEqual(str(e.exception), 'You are supposed to decrease the price!')
        self.assertEqual(self.car.price, 10000)

    def test_set_promotional_price_valid(self):
        self.assertEqual(self.car.price, 10000)
        self.assertEqual(self.car.set_promotional_price(9999), 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 9999)

    def test_need_repair_invalid(self):
        self.assertEqual(self.car.need_repair(5001, 'repair'), 'Repair is impossible!')
        self.assertEqual(self.car.price, 10000)
        self.assertEqual(self.car.repairs, [])
        self.assertEqual(len(self.car.repairs), 0)

    def test_need_repair_valid(self):
        self.assertEqual(self.car.need_repair(1000, 'repair'), 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 11000)
        self.assertEqual(self.car.repairs, ['repair'])
        self.assertEqual(len(self.car.repairs), 1)

    def test_need_repair_add_repair_description(self):
        self.assertEqual(self.car.need_repair(1000, 'repair'), 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 11000)
        self.assertEqual(self.car.repairs, ['repair'])
        self.assertEqual(len(self.car.repairs), 1)

        self.assertEqual(self.car.need_repair(500, 'another repair'), 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 11500)
        self.assertEqual(self.car.repairs, ['repair', 'another repair'])
        self.assertEqual(len(self.car.repairs), 2)

    def test_gt_invalid(self):
        car_two = SecondHandCar('Mercedes', "hathback", 1000, 10000)
        self.assertEqual(self.car > car_two, 'Cars cannot be compared. Type mismatch!')

    def test_gt_valid(self):
        self.assertTrue(self.car > self.car2)

    def test_str(self):
        self.assertEqual(str(self.car), "Model BMW | Type Sedan | Milage 1000km\nCurrent price: 10000.00 | Number of "
                                        "Repairs: 0")
