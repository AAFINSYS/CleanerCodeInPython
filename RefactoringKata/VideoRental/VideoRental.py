class Rental:
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def movie(self):
        return self._movie

    @property
    def days_rented(self):
        return self._days_rented


class Movie:
    Regular = 0
    NewRelease = 1
    Children = 2

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    @property
    def title(self):
        return self._title

    @property
    def price_code(self):
        return self._price_code

    @price_code.setter
    def price_code(self, new_value):
        self._price_code = new_value


class Customer:
    def __init__(self, name):
        self._name = name
        self._rentals = []

    @property
    def name(self):
        return self._name

    def add_rental(self, rental):
        self._rentals.append(rental)

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0

        result = "Rental Record for " + self._name + "\n"
        for rental in self._rentals:
            amount = 0

            # determine amounts for each line
            if rental.movie.price_code == Movie.Regular:
                amount += 2
                if rental.days_rented > 2:
                    amount += (rental.days_rented - 2) * 1.5
            elif rental.movie.price_code == Movie.NewRelease:
                amount += rental.days_rented * 3
            elif rental.movie.price_code == Movie.Children:
                amount += 1.5
                if rental.days_rented > 3:
                    amount += (rental.days_rented - 3) * 1.5

            this_amount = amount

            # add frequent renter points
            frequent_renter_points += 1

            # add bonus for a two day new release rental
            if rental.movie.price_code == Movie.NewRelease and rental.days_rented > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + rental.movie.title + "\t" + str(this_amount) + "\n";
            total_amount += this_amount;

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n";
        result += "You earned " + str(frequent_renter_points) + " frequent renter points";
        return result
