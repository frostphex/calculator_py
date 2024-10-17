import math
import random


def find_square_root():
    """Returns square root of a number."""
    print("Enter the number:")
    number = float(input("> "))
    return math.sqrt(number)


def find_absolute_value():
    """Returns absolute value of a number."""
    print("Enter the number:")
    number = float(input("> "))
    return abs(number)


def find_sine():
    """Returns sine of a number"""
    number = int(input("> "))
    return math.sin(number)


def find_cosine():
    """Returns sine of a number"""
    number = int(input("> "))
    return math.cos(number)


def find_tangent():
    """Returns sine of a number"""
    number = int(input("> "))
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
