import unittest
from RefactoringKata.VideoRental.VideoRental import Customer, Rental, Movie


class Test_VideoRental(unittest.TestCase):
    def test_should_when(self):
        customer = Customer("John")
        movie = Movie("Fantasia", Movie.Children)
        rental = Rental(movie, 1)

        customer.add_rental(rental)

        actual = customer.statement()

        self.assertEqual(actual, "Rental Record for John\n\tFantasia\t1.5\nAmount owed is 1.5\nYou earned 1 frequent renter points")

if __name__ == "__main__":
    unittest.main()