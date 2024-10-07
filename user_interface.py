def ask_choice():
    """Returns None if an invalid choice is made by the user.."""
    try:
        choice = int(input("> "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please select a valid option.")
            return None
        return choice
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None


def display_options():
    """Display calculator options to the user"""
    OPTIONS = ("Addition", "Subtraction", "Division", "Multiplication", "Exit")
    print("\nPlease select a calculator function to calculate: ")
    for index, option in enumerate(OPTIONS, start=1):
        print(f"{index}. {option}")


def confirm_exit():
    """Returns a boolean if the user wants to exit the calculator or not."""
    should_exit = input("Do you really want to exit calculator? (yes/no): ")
    return should_exit[0].lower() == "y"


def get_number(prompt):
    """Helper function to get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Enter a valid number.")
