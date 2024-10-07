import user_interface as ui
from calculator import Calculator


def main():
    print(f"{'*' * 20} Calculator Project {'*' * 20}")

    # Prompt the user to enter two numbers
    num1 = ui.get_number("First number: ")
    num2 = ui.get_number("Second number: ")

    calculator = Calculator(num1, num2)
    is_active = True

    while is_active:
        ui.display_options()

        choice = ui.ask_choice()
        if choice is None:
            continue  # Return to menu if the choice is invalid

        if choice == 6:
            # Confirm before exiting
            if ui.confirm_exit():
                print("Exiting calculator. Have a great day!")
                is_active = False
            continue

        if choice == 5:
            # Enter new numbers
            num1 = ui.get_number("First number: ")
            num2 = ui.get_number("Second number: ")
            calculator = Calculator(num1, num2)
            continue

        # Perform the calculation based on the choice
        result = calculator.calculate(choice)
        if result is not None:
            print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
