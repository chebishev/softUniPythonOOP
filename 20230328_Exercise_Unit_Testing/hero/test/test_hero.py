from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Superman", 2, 10, 5)
        self.enemy = Hero("Batman", 3, 20, 10)

    def test_init(self):
        self.assertEqual("Superman", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_same_username(self):
        with self.assertRaises(Exception) as e:
            hero = Hero("Superman", 2, 10, 5)
            self.hero.battle(hero)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_battle_hero_health_zero_or_bellow(self):
        with self.assertRaises(ValueError) as ve:
            self.hero.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_health_zero_or_bellow(self):
        with self.assertRaises(ValueError) as ve:
            self.enemy.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Batman. He needs to rest", str(ve.exception))

    def test_battle_both_bellow_zero(self):
        self.hero.health = 1
        self.enemy.health = 1
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_defeat_enemy(self):
        enemy = Hero("Batman", 2, 5, 1)
        self.assertEqual("You win", self.hero.battle(enemy))
        self.assertEqual(3, self.hero.level)
        self.assertEqual(13, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_lose(self):
        self.hero.health = 1
        self.assertEqual("You lose", self.hero.battle(self.enemy))
        self.assertEqual(4, self.enemy.level)
        self.assertEqual(15, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test__str__method_for_correct_message(self):
        self.assertEqual("Hero Superman: 2 lvl\n" +
                         "Health: 10\n" +
                         "Damage: 5\n", str(self.hero))


if __name__ == "__main__":
    main()
