def is_numeric(value):
    """Validate if input is numeric."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def get_numeric_input(prompt):
    """Get and validate numeric input from user."""
    while True:
        user_input = input(prompt)
        if is_numeric(user_input):
            return float(user_input)
        else:
            print(f"Invalid input: '{user_input}' is not numeric. Please enter a valid number.")


def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract two numbers."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide two numbers with zero check."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("-" * 30)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option.")
            continue
        
        try:
            num1 = get_numeric_input("Enter first number: ")
            num2 = get_numeric_input("Enter second number: ")
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
