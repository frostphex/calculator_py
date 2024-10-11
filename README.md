# CLI Calculator using Python

A simple calculator program built with Python that performs basic mathematical
operations such as addition, subtraction, multiplication, and division. This
project is designed with an easy-to-use interface and handles common exceptions
like division by zero.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first number.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second number (with division by zero handling).
- **New Numbers**: Asks two new numbers from the user.
- **Exit Option**: Allows the user to confirm before exiting.

## Installation

1. Clone the repository:
   ```bash
      git clone https://github.com/frostphex/calculator_py.git
   ```
2. Make sure you have Python 3.11 or newer installed. If not, you can 
   download it from [here](https://www.python.org/downloads/).

3. Run the calculator:
   ```bash
   cd calculator_py/src
   python3 main.py
   ```

## Usage

Upon running the program, you will be prompted to input two numbers. 
After that, you can select from the available calculator options:

1. Addition
2. Subtraction
3. Division
4. Multiplication
5. New Numbers
6. Exit

If you attempt to divide by zero, the program will catch the error
and notify you.

### Example

```
******************** Calculator Project ********************
Please enter two numbers:
First number: 10
Second number: 5

Please select a calculator function to calculate:

1. Addition
2. Subtraction
3. Division
4. Multiplication
5. New Numbers
6. Exit

> 1

Result: 15
```

## Code Structure

[calculator.py](./src/calculator.py) - Contains the logic for mathematical operations.

[user_interface.py](./src/user_interface.py) - Handles user input and displays options to the user.

[main.py](./src/main.py) - The main script to run the calculator.

## Future Enhancements

- Add support for more advanced operations (e.g., square roots, powers).
- Implement a graphical user interface (GUI) using a library like Tkinter or PyQt.
- Include support for complex numbers.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file 
for details.

---

Feel free to fork and contribute to this project!
