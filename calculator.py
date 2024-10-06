# Calculator Project

# Basic functions - add, subtract, divide, multiply

class Calculator:
  """A class to perform basic calculations operations."""
  def __init__(self, num1, num2):
    """Initialize the numbers for operations."""
    self.num1 = num1
    self.num2 = num2
    
  def display_options(self):
    """Display calculator options to the user"""
    print("\nPlease select a calculator function to calculate: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    
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
    if choice == 1:
      return self.add()
    elif choice == 2:
      return self.subtract()
    elif choice == 3:
      return self.divide()
    elif choice == 4:
      return self.multiply()

print(f"{'*' * 20} Calculator Project {'*' * 20}")
print("Please enter two numbers:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
calculator = Calculator(num1, num2)

while True:
  calculator.display_options()

  try:
    choice = int(input("> "))
    if choice not in [1, 2, 3, 4, 5]:
      print("Invalid choice. Please select a valid option.")
      continue
  except ValueError:
    print("Error: Invalid input. Please enter a number.")
    continue
  else:
    if choice == 5:
      confirm_exit = input("Do you really want to exit calculator? (yes/no): ")
      if confirm_exit[0].lower() == "y":
        print("Exiting calculator. Have a great day!")
        break
      
    result = calculator.calculate(choice)  
    if result is not None:
      print(f"\nResult: {result}")
