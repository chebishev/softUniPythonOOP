from unittest import TestCase, main
from horse_racings.project import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Jorge", "Dog", "Woof")

    def test_initialization(self):
        self.assertEqual(self.mammal.name, "Jorge")
        self.assertEqual(self.mammal.type, "Dog")
        self.assertEqual(self.mammal.sound, "Woof")

    def test_if_make_sound_returns_correct_message(self):
        self.assertEqual(self.mammal.make_sound(), "Jorge makes Woof")

    def test_if_get_kingdom_returns_the_private_attribute(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_if_info_returns_correct_message(self):
        self.assertEqual(self.mammal.info(), "Jorge is of type Dog")


if __name__ == "__main__":
    main()
