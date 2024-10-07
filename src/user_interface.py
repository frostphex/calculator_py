def ask_choice():
    """Returns user's choice if valid, otherwise None."""
    try:
        choice = int(input("> "))
        if choice not in range(1, 7):  # Valid options: 1, 2, 3, 4, 5, 6
            print("Invalid choice. Please select a valid option (1-6).")
            return None
        return choice
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None


def display_options():
    """Display calculator options to the user."""
    OPTIONS = ("Addition", "Subtraction", "Division", "Multiplication", "New Numbers" ,"Exit")
    print("\nPlease select a calculator function to calculate:")
    for index, option in enumerate(OPTIONS, start=1):
        print(f"{index}. {option}")


def confirm_exit():
    """Returns True if the user wants to exit the calculator, False otherwise."""
    while True:
        should_exit = input("Do you really want to exit the calculator? (yes/no): ").lower()
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
