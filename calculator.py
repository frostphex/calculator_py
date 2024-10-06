# Calculator Project

# Basic functions - add, subtract, divide, multiply


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
            print("Error: Division by zero is not allowed.")
        else:
            return result

    def multiply(self):
        """Returns product of two numbers."""
        return self.num1 * self.num2

    def calculate(self, choice):
        """Calculates the result of two numbers."""
        operations = {
            1: self.add,
            2: self.subtract,
            3: self.divide,
            4: self.multiply,
            5: self.exit,
        }
        return operations[choice]()

    def ask_choice(self):
        """Asks user a operation choice, returns -1 if invalid."""
        try:
            choice = int(input("> "))
            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please select a valid option.")
                return -1
            return choice
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            return -1

    def display_options(self):
        """Display calculator options to the user"""
        print("\nPlease select a calculator function to calculate: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Exit")

    def exit(self):
        """Returns boolean if the user wants to exit the calculator. True if they want to exit the calculator."""
        confirm_exit = input("Do you really want to exit calculator? (yes/no): ")
        return confirm_exit[0].lower() == "y"


def get_number(prompt):
    """Helper function to get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Enter a valid number.")


if __name__ == "__main__":
    print(f"{'*' * 20} Calculator Project {'*' * 20}")
    print("Please enter two numbers:")

    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")

    calculator = Calculator(num1, num2)

    while True:
        calculator.display_options()

        choice = calculator.ask_choice()
        if choice == -1:
            continue

        result = calculator.calculate(choice)
        if result == True:
            print("Exiting calculator. Have a great day!")
            break
        if result is not None:
            print(f"\nResult: {result}")
