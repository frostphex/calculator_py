import user_interface as ui
from calculator import Calculator


def main():
    print(f"{'*' * 20} Calculator Project {'*' * 20}")
    print("Please enter two numbers:")

    num1 = ui.get_number("First number: ")
    num2 = ui.get_number("Second number: ")

    calculator = Calculator(num1, num2)
    is_active = True

    while is_active:
        ui.display_options()

        choice = ui.ask_choice()
        if not choice:
            continue

        result = calculator.calculate(choice)
        if result == True and type(result) == bool:
            print("Exiting calculator. Have a great day!")
            is_active = False
        elif result is not None:
            print(f"\nResult: {result}")


main()
