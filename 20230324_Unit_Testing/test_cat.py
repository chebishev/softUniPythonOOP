class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Tom')

    def test_increase_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_error_if_already_fed(self):
        with self.assertRaises(Exception) as e:
            self.cat.eat()
            self.cat.eat()
        self.assertEqual(str(e.exception), 'Already fed.')

    def test_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as e:
            self.cat.sleep()
        self.assertEqual(str(e.exception), 'Cannot sleep while hungry')

    def test_sleepy_cat_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == '__main__':
    unittest.main()
