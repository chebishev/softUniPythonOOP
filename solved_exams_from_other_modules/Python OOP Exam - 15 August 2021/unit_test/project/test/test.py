from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Rex")

    def test_init(self):
        self.assertEqual(self.pet_shop.name, "Rex")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_invalid_qty(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food('food', 0)
        self.assertEqual(str(context.exception), "Quantity cannot be equal to or less than 0")

    def test_non_existing_name(self):
        result = self.pet_shop.add_food('Food', 20)
        self.assertEqual(result, "Successfully added 20.00 grams of Food.")
        self.assertEqual(self.pet_shop.food, {'Food': 20})

    def test_existing_name(self):
        self.pet_shop.food = {"food": 15}
        self.assertEqual(self.pet_shop.add_food("food", 8),
                         "Successfully added 8.00 grams of food.")
        self.assertEqual(self.pet_shop.food, {"food": 23})

    def test_add_pet_with_non_existing_name(self):
        result = self.pet_shop.add_pet('Sheri')
        self.assertEqual(result, "Successfully added Sheri.")
        self.assertEqual(self.pet_shop.pets, ['Sheri'])

    def test_add_pet_with_existing_name(self):
        self.pet_shop.add_pet('Sheri')
        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet('Sheri')
        self.assertEqual(str(context.exception), "Cannot add a pet with the same name")

    def test_feed_pet_missing_pet(self):
        with self.assertRaises(Exception) as e:
            self.pet_shop.feed_pet("Woof", "food")
        self.assertEqual(str(e.exception), "Please insert a valid pet name")

    def test_feed_pet_missing_food(self):
        self.pet_shop.pets = ["Woof"]
        self.assertEqual(self.pet_shop.feed_pet("food", "Woof"),
                         "You do not have food")

    def test_not_enough_qty_food(self):
        self.pet_shop.add_pet('Buddy')
        self.pet_shop.food = {'Food': 90}
        result = self.pet_shop.feed_pet('Food', 'Buddy')
        self.assertEqual(result, "Adding food...")
        self.assertEqual(self.pet_shop.food, {'Food': 1090.00})

    def test_feed_pet_enough_qty(self):
        self.pet_shop.add_pet("Woof")
        self.pet_shop.add_food("Fish", 120)
        self.assertEqual(self.pet_shop.feed_pet("Fish", "Woof"),
                         "Woof was successfully fed")
        self.assertEqual(self.pet_shop.food, {"Fish": 20})

    def test_repr_(self):
        self.pet_shop.add_pet("Sheri")
        self.pet_shop.add_pet("Jerry")
        self.assertEqual(repr(self.pet_shop),
                         'Shop Rex:\n'
                         'Pets: Sheri, Jerry')

