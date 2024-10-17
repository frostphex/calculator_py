import math
import random


def find_square_root(number):
    """Returns square root of a number."""
    return math.sqrt(number)


def find_absolute_value(number):
    """Returns absolute value of a number."""
    return abs(number)


def find_sine(number):
    """Returns sine of a number"""
    return math.sin(number)


def find_cosine(number):
    """Returns cosine of a number"""
    return math.cos(number)


def find_tangent(number):
    """Returns tan of a number"""
    return math.tangent(number)


def calculate_exponentiation():
    """Returns a number raised to the power."""
    print("Enter base:")
    base = float(input("> "))

    print("Enter power:")
    power = float(input("> "))
    return math.pow(base, power)


def calculate_log():
    """Returns a log of a number."""
    print("Enter number:")
    number = float(input("> "))

    print("Enter base:")
    base = float(input("> "))
    return math.log(number, base)


def calculate_factorial():
    """Returns the factorial of a number."""
    print("Enter the number:")
    try:
        number = int(input("> "))
    except ValueError:
        print("Please enter a number without decimal.")
    else:
        return math.factorial(number)


def generate_random_number():
    """Returns a random number."""
    try:
        min_range = int(input("Enter a minimum range:\n> "))
        max_range = int(input("Enter a maximum range:\n> "))
    except ValueError:
        print("Please enter a number without decimal.")
    else:
        return random.randint(min_range, max_range)
