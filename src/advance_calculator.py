import math
import random


class AdvanceCalculator:
    """A class to perform advance mathematical operations."""

    def __init__(self, number):
        """Initialize with a number."""
        self.number = number

    def find_square_root(self):
        """Returns square root of a number."""
        return math.sqrt(self.number)

    def find_absolute_value(self):
        """Returns absolute value of a number."""
        return abs(self.number)

    def find_sine(self):
        """Returns sine of a number"""
        return math.sin(self.number)

    def find_cosine(self):
        """Returns cosine of a number"""
        return math.cos(self.number)

    def find_tangent(self):
        """Returns tan of a number"""
        return math.tan(self.number)

    @staticmethod
    def calculate_exponentiation(base, power):
        """Returns a number raised to the power."""
        return math.pow(base, power)

    @staticmethod
    def calculate_log(number, base):
        """Returns a log of a number."""
        if number <= 0 or base <= 0:
            raise ValueError("Number and base must be greater than zero.")
        return math.log(number, base)

    @staticmethod
    def calculate_factorial(number):
        """Returns the factorial of a number."""
        if number < 0:
            raise ValueError("Number must be non-negative.")
        return math.factorial(number)

    @staticmethod
    def generate_random_number(min_range, max_range):
        """Returns a random number."""
        if min_range > max_range:
            raise ValueError("Minimum range should be less than maximum range.")
        return random.randint(min_range, max_range)
