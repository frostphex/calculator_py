from calculator import Calculator
from advance_calculator import AdvanceCalculator

_NEW_OPTIOns = {
    1: "Arithmetic",
    2: "Trigonometric",
    3: "Logarithmic",
    4: "Exit",
    # 5: "Statistic",
    # 6: "Matrix",
    # 7: "Complex number",
}

_BASIC_OPTIONS = {
    1: "Addition",
    2: "Subtraction",
    3: "Division",
    4: "Multiplication",
    5: "New Numbers",
    6: "Back",
}

_TRIG_OPTIONS = {
    1: "Sine",
    2: "Cosine",
    3: "Tangent",
    4: "Square Root",
    5: "Back",
}

_LOG_OPTIONS = {
    1: "Logarithm",
    2: "Exponentiation",
    3: "Factorial",
    4: "Back",
}


def ask_choice(options):
    """Returns user's choice if valid, otherwise None."""
    try:
        choice = int(input("> "))
        if choice not in options:
            first, *_, last = options.keys()
            print(f"Invalid choice. Please select a valid option ({first}-{last}).")
            return None
        return choice
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None


def display_options(options):
    """Display calculator options to the user."""
    print("\nPlease select a calculator function to calculate:")
    for index, option in options.items():
        print(f"{index}. {option}")


def basic_operations_menu():
    """Menu for basic arithmetic operations."""
    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")
    calculator = Calculator(num1, num2)
    is_active = True

    while is_active:
        display_options(_BASIC_OPTIONS)
        choice = ask_choice(_BASIC_OPTIONS)
        if choice in range(1, 5):
            result = calculator.calculate(choice)
            if result is not None:
                print(f"\nResult: {result}")
        elif choice == 5:
            # Enter new numbers
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            calculator = Calculator(num1, num2)
            continue
        elif choice == 6:
            break


def trigonometric_menu():
    """Menu for trigonometric operations."""
    number = get_number("Enter the number (in radians): ")
    adv_calc = AdvanceCalculator(number)
    is_active = True

    while is_active:
        display_options(_TRIG_OPTIONS)
        choice = ask_choice(_TRIG_OPTIONS)
        match choice:
            case 1:
                print(f"Sine : {adv_calc.find_sine()}")
            case 2:
                print(f"CoSine : {adv_calc.find_cosine()}")
            case 3:
                print(f"Sine : {adv_calc.find_tangent()}")
            case 4:
                print(f"Square root : {adv_calc.find_square_root()}")


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
