# Copilot Agent Demo

A simple Python calculator project demonstrating basic arithmetic operations with input validation.

## Features

- **Add**: Add two numbers
- **Subtract**: Subtract two numbers
- **Multiply**: Multiply two numbers
- **Divide**: Divide two numbers with zero check protection
- **Input Validation**: Validates that all inputs are numeric before processing

## Requirements

Python 3.6+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Divya-Shivanuri/copilot-agent-demo.git
cd copilot-agent-demo
```

2. Run the calculator:
```bash
python main.py
```

## Usage

Run the program and follow the interactive menu to select an operation:

```
Simple Calculator
------------------------------

Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
```

Enter your choice and provide two numbers for the calculation. The program will validate that your inputs are numeric.

## Input Validation

The calculator includes robust input validation:
- **Numeric Check**: The `is_numeric()` function ensures all numeric inputs are valid numbers
- **Validation Loop**: The `get_numeric_input()` function keeps prompting until valid input is received
- **Division by Zero**: Prevents division by zero operations
- **Invalid Menu Choice**: Validates menu selections

Example of validation in action:
```
Enter first number: abc
Invalid input: 'abc' is not numeric. Please enter a valid number.
Enter first number: 42
```

## License

MIT License
