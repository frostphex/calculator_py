#!/usr/bin/env python3
# calculator.py - A calculator program to perform basic operations on numbers.


class Calculator:
    """A class to perform basic mathematical operations."""

    def __init__(self, num1, num2):
        """Initialize the two numbers for operations."""
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Returns the sum of two numbers."""
        return self.num1 + self.num2

    def subtract(self):
        """Returns the difference between two numbers."""
        return self.num1 - self.num2

    def divide(self):
        """Returns the division of two numbers. Handles division by zero."""
        try:
            result = self.num1 / self.num2
        except ZeroDivisionError:
            result = None
            print("Error: Division by zero is not allowed.")
        return result

    def multiply(self):
        """Returns the product of two numbers."""
        return self.num1 * self.num2

    def calculate(self, choice):
        """Calculates the result based on the user's choice."""
        result = None

        # Match user choice to the appropriate operation
        match choice:
            case 1:
                result = self.add()
            case 2:
                result = self.subtract()
            case 3:
                result = self.divide()
            case 4:
                result = self.multiply()

        return result
