# /usr/bin/env python3
# calculator.py - A calculator program to perform basic operations on numbers.

import user_interface as ui


class Calculator:
    """A class to perform basic calculations operations."""

    def __init__(self, num1, num2):
        """Initialize the numbers for operations."""
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Returns addition of two numbers."""
        return self.num1 + self.num2

    def subtract(self):
        """Returns difference of two numbers."""
        return self.num1 - self.num2

    def divide(self):
        """Returns division of two numbers."""
        try:
            result = self.num1 / self.num2
        except ZeroDivisionError:
            result = None
            print("Error: Division by zero is not allowed.")
        return result

    def multiply(self):
        """Returns product of two numbers."""
        return self.num1 * self.num2

    def calculate(self, choice):
        """Calculates the result of two numbers."""
        result = None

        match choice:
            case 1:
                result = self.add()
            case 2:
                result = self.subtract()
            case 3:
                result = self.divide()
            case 4:
                result = self.multiply()
            case 5:
                result = ui.confirm_exit()

        return result
