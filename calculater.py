class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""
    
    @staticmethod
    def add(x: float, y: float) -> float:
        """Add two numbers."""
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        """Subtract two numbers."""
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """Multiply two numbers."""
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        """Divide two numbers."""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

    def display_menu(self) -> None:
        """Display the calculator menu."""
        print("\nCalculator Operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def get_numbers(self) -> tuple[float, float]:
        """Get two numbers from user input."""
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
            except ValueError:
                print("Invalid input! Please enter numeric values.")

    def get_valid_choice(self) -> str:
        """Get and validate user's operation choice."""
        valid_choices = {'1', '2', '3', '4', '5'}
        while True:
            choice = input("Enter choice (1/2/3/4/5): ")
            if choice in valid_choices:
                return choice
            print("Invalid input! Please select a valid operation (1-5).")

    def calculate(self, choice: str, x: float, y: float) -> float | None:
        """Perform the calculation based on user choice."""
        operations = {
            '1': (self.add, '+'),
            '2': (self.subtract, '-'),
            '3': (self.multiply, '*'),
            '4': (self.divide, '/')
        }
        
        if choice not in operations:
            return None
            
        operation_func, operator = operations[choice]
        try:
            result = operation_func(x, y)
            print(f"\nResult: {x} {operator} {y} = {result}")
            return result
        except ValueError as e:
            print(f"\nError: {e}")
            return None

    def get_continue_choice(self) -> bool:
        """Get and validate user's choice to continue or exit."""
        while True:
            choice = input("\nWould you like to perform another calculation? (y/n): ").lower()
            if choice == 'y':
                return True
            if choice == 'n':
                return False
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")


def main():
    """Main function to run the calculator program."""
    calculator = Calculator()
    
    print("Welcome to the Calculator Program!")
    
    while True:
        calculator.display_menu()
        choice = calculator.get_valid_choice()
        
        if choice == '5':
            print("\nThank you for using the calculator!")
            break
            
        num1, num2 = calculator.get_numbers()
        calculator.calculate(choice, num1, num2)
        
        if not calculator.get_continue_choice():
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    main()