
_OPTIONS = {
    1: "Addition",
    2: "Subtraction",
    3: "Division",
    4: "Multiplication",
    5: "New Numbers",
    6: "Exit",
}


def ask_choice():
    """Returns user's choice if valid, otherwise None."""
    try:
        choice = int(input("> "))
        if choice not in _OPTIONS:
            first, *_, last = _OPTIONS.keys()
            print(f"Invalid choice. Please select a valid option ({first}-{last}).")
            return None
        return choice
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None


def display_options():
    """Display calculator options to the user."""
    print("\nPlease select a calculator function to calculate:")
    for index, option in _OPTIONS.items():
        print(f"{index}. {option}")


def confirm_exit():
    """Returns True if the user wants to exit the calculator, False otherwise."""
    while True:
        should_exit = input(
            "Do you really want to exit the calculator? (yes/no): "
        ).lower()
        if should_exit in ["yes", "y"]:
            return True
        elif should_exit in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def get_number(prompt):
    """Helper function to get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Enter a valid number.")

def ask_single_number():
    """Returns a user input number. """
    print("Enter the number:")
    number = float(input("> "))
    return number
