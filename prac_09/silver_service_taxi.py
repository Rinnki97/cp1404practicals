from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ Represents a type of taxi that includes additional services and charges."""
    flagfall = 4.5

    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate and return the fare of the taxi ride. Includes the flagfall charge."""
        fare = super().get_fare()
        fare += self.flagfall
        return fare

    def __str__(self):
        """Return a formatted string representing the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"


