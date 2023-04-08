from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("John", 18, 100)

    def test_init(self):
        self.assertEqual(self.player.name, "John")
        self.assertEqual(self.player.age, 18)
        self.assertEqual(self.player.points, 100)
        self.assertEqual(self.player.wins, [])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Jo", 18, 100)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("John", 15, 100)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_valid(self):
        self.player.add_new_win("Tennis World Cup")
        self.player.add_new_win("Tennis World Cup 2")
        self.assertEqual(self.player.wins, ["Tennis World Cup", "Tennis World Cup 2"])

    def test_existing_win(self):
        self.player.add_new_win("Tennis World Cup")
        self.assertEqual(self.player.add_new_win("Tennis World Cup"),
                         "Tennis World Cup has been already added to the list of wins!")
        self.assertEqual(self.player.wins, ["Tennis World Cup"])

    def test__lt__valid(self):
        player1 = TennisPlayer("Jim", 18, 111)
        self.assertEqual(self.player.__lt__(player1),
                         "Jim is a top seeded player and he/she is better than John")

    def test__lt__other_wins(self):
        player1 = TennisPlayer("Jim", 18, 99)
        self.assertEqual(self.player.__lt__(player1), "John is a better player than Jim")

    def test__str__(self):
        self.player.add_new_win("Tennis World Cup")
        self.player.add_new_win("Tennis World Cup 2")
        self.assertEqual(self.player.__str__(), "Tennis Player: John\n"
                                                "Age: 18\n"
                                                "Points: 100.0\n"
                                                "Tournaments won: Tennis World Cup, Tennis World Cup 2")


if __name__ == "__main__":
    main()
