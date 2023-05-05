from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory
from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.pf = PaintFactory("PaintFactory", 100)

    def test_init(self):
        self.assertEqual(self.pf.name, "PaintFactory")
        self.assertEqual(self.pf.capacity, 100)
        self.assertEqual(self.pf.ingredients, {})

    def test_add_ingredient_not_valid(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient("black", 12)
        self.assertEqual(str(te.exception), "Ingredient of type black not allowed in PaintFactory")

    def test_add_ingredient_not_enough_space(self):
        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient("white", 112)
        self.assertEqual(str(ve.exception), "Not enough space in factory")

    def test_add_ingredient(self):
        self.pf.add_ingredient("white", 12)
        self.assertEqual(self.pf.ingredients, {"white": 12})
        self.pf.add_ingredient("white", 12)
        self.assertEqual(self.pf.products, {"white": 24})

    def test_remove_ingredient_missing(self):
        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient("white", 12)
        self.assertEqual(str(ke.exception), "'No such ingredient in the factory'")

    def test_test_remove_ingredient_more_quantity(self):
        self.pf.ingredients = {"white": 12}
        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient("white", 13)
        self.assertEqual(str(ve.exception), "Ingredients quantity cannot be less than zero")
        self.assertEqual(self.pf.ingredients, {"white": 12})

    def test_remove_ingredient_valid(self):
        self.pf.add_ingredient("white", 12)
        self.pf.add_ingredient("yellow", 12)
        self.pf.remove_ingredient("white", 12)
        self.assertEqual(self.pf.ingredients, {"white": 0, "yellow": 12})

    def test_can_add_false(self):
        self.pf.capacity = 1
        self.assertFalse(self.pf.can_add(12))

    def test_can_add_valid(self):
        self.assertTrue(self.pf.can_add(12))

    def test_repr(self):
        self.pf.add_ingredient("white", 12)
        self.pf.add_ingredient("yellow", 12)
        self.assertEqual(self.pf.__repr__(),
                         "Factory name: PaintFactory with capacity 100.\nwhite: 12\nyellow: 12\n")
