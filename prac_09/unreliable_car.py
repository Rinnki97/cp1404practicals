import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Represents a type of car that might not always be able to drive due to its unreliable nature."""
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar with a given name, amount of fuel, and reliability factor."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car a certain distance."""
        if random.uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0
