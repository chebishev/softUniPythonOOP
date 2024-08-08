from collections import deque
from unittest import TestCase
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def test_valid_name(self):
        station = RailwayStation("Sofia")
        self.assertEqual("Sofia", station.name)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            station = RailwayStation("S")
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_arrival_trains_list(self):
        station = RailwayStation("Sofia")
        station.new_arrival_on_board("Nov Vlak")
        self.assertEqual(1, len(station.arrival_trains))

    def test_invalid_train(self):
        station = RailwayStation("Sofia")
        station.new_arrival_on_board("Nov Vlak")
        station.new_arrival_on_board("Star Vlak")
        self.assertEqual("There are other trains to arrive before Star Vlak.", station.train_has_arrived("Star Vlak"))

    def test_valid_train(self):
        station = RailwayStation("Sofia")
        station.new_arrival_on_board("Nov Vlak")
        station.new_arrival_on_board("Star Vlak")
        self.assertEqual("Nov Vlak is on the platform and will leave in 5 minutes.",
                         station.train_has_arrived("Nov Vlak"))

    def test_valid_train_left(self):
        station = RailwayStation("Sofia")
        station.new_arrival_on_board("Nov Vlak")
        station.new_arrival_on_board("Star Vlak")
        station.train_has_arrived("Nov Vlak")
        station.train_has_arrived("Star Vlak")
        self.assertTrue(station.train_has_left("Nov Vlak"))

    def test_invalid_train_left(self):
        station = RailwayStation("Sofia")
        station.new_arrival_on_board("Nov Vlak")
        station.train_has_arrived("Nov Vlak")
        self.assertFalse(station.train_has_left("Star Vlak"))
