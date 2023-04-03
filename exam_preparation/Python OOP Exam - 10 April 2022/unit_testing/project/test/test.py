from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("The Matrix", 1999, 8.5)

    def test_initialization(self):
        self.assertEqual(self.movie.name, "The Matrix")
        self.assertEqual(self.movie.year, 1999)
        self.assertEqual(self.movie.rating, 8.5)
        self.assertEqual(self.movie.actors, [])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            movie = Movie("", 1999, 8.5)
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_invalid_year(self):
        with self.assertRaises(ValueError) as ve:
            movie = Movie("The Matrix", 1886, 8.5)
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_existing(self):
        self.movie.actors.append("Keanu Reeves")
        self.assertEqual(self.movie.add_actor("Keanu Reeves"), "Keanu Reeves is already added in the list of actors!")
        self.assertEqual(self.movie.actors, ["Keanu Reeves"])

    def test_add_actor_valid(self):
        self.movie.add_actor("Keanu Reeves")
        self.assertEqual(self.movie.actors, ["Keanu Reeves"])

    def test__gt__method_other_higher_rating(self):
        movie2 = Movie("The Matrix 2", 2000, 8.6)
        self.assertEqual(self.movie.__gt__(movie2), '"The Matrix 2" is better than "The Matrix"')

    def test__gt__method_self_higher_rating(self):
        movie1 = Movie("The Matrix 3", 1999, 8.3)
        self.assertEqual(self.movie.__gt__(movie1), '"The Matrix" is better than "The Matrix 3"')

    def test__repr__(self):
        self.movie.add_actor("Laurence Fishburne")
        self.movie.add_actor("Keanu Reeves")
        self.assertEqual(self.movie.__repr__(), "Name: The Matrix\n"
                                                "Year of Release: 1999\n"
                                                "Rating: 8.50\n"
                                                "Cast: Laurence Fishburne, Keanu Reeves")


if __name__ == "__main__":
    main()
