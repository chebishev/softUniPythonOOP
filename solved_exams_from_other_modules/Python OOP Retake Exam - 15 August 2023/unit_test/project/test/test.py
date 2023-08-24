from unittest import TestCase

from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(1000, 2, True)
        self.trip2 = Trip(1000, 1, False)

    def test_init(self):
        self.assertEqual(self.trip.budget, 1000)
        self.assertEqual(self.trip.travelers, 2)
        self.assertTrue(self.trip.is_family)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_travelers_invalid(self):
        with self.assertRaises(ValueError) as ex:
            trip = Trip(1000, 0, True)
        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_is_family(self):
        trip = Trip(1000, 1, True)
        self.assertFalse(trip.is_family)

    def test_book_a_trip_invalid_destination(self):
        self.assertEqual(self.trip.book_a_trip("Ibiza"),
                         'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_not_enough_budget(self):
        self.assertEqual(self.trip.book_a_trip("New Zealand"), 'Your budget is not enough!')

    def test_book_a_trip_family(self):
        self.assertEqual(self.trip.book_a_trip('Bulgaria'),
                         'Successfully booked destination Bulgaria! Your budget left is 100.00')

    def test_book_a_trip_not_family(self):
        self.assertEqual(self.trip2.book_a_trip('Bulgaria'),
                         'Successfully booked destination Bulgaria! Your budget left is 500.00')

    def test_booking_status_empty(self):
        self.assertEqual(self.trip.booking_status(), 'No bookings yet. Budget: 1000.00')

    def test_booking_status_one_item(self):
        self.trip2.book_a_trip('Bulgaria')
        self.assertEqual(self.trip2.booking_status(),
                         "Booked Destination: Bulgaria\n"
                         "Paid Amount: 500.00\n"
                         "Number of Travelers: 1\n"
                         "Budget Left: 500.00")

    def test_booking_status_sorting(self):
        trip = Trip(12000, 1, False)
        trip.book_a_trip('Bulgaria')
        trip.book_a_trip('Brazil')
        self.assertEqual(trip.booking_status(),
                         "Booked Destination: Brazil\n"
                         "Paid Amount: 6200.00\n"
                         "Booked Destination: Bulgaria\n"
                         "Paid Amount: 500.00\n"
                         "Number of Travelers: 1\n"
                         "Budget Left: 5300.00")
