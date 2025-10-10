# Personal Expense Tracker

A personal expense tracking system using Object-Oriented Programming and unit testing.

## Features

### Core Functionality
- **Add Expense**: Allows users to add new expense records with description, amount, and category
- **Calculate Total Expense**: Computes and displays the total amount of all recorded expenses

### Additional Features
- Category-based expense management
- Query and statistics by category
- Detailed expense summary display
- Clear all expense records
- Interactive user interface

## File Structure

```
├── expense_tracker.py      # Main class definitions (Expense and ExpenseTracker)
├── test_expense_tracker.py # Unit test file
├── main.py                 # Main program demonstration file
├── demo.py                 # Core functionality demo script
└── README.md              # Documentation
```

## Class Design

### Expense Class
Represents a single expense record with the following attributes:
- `description`: Expense description
- `amount`: Expense amount
- `category`: Expense category
- `date`: Expense date and time

### ExpenseTracker Class
Main class for managing expense records, providing the following methods:
- `add_expense()`: Add new expense
- `calculate_total_expense()`: Calculate total expenses
- `get_expenses_by_category()`: Get expenses by category
- `get_total_by_category()`: Calculate total by category
- `display_summary()`: Display expense summary
- `clear_all_expenses()`: Clear all records

## Usage

### 1. Run Unit Tests
```bash
python -m pytest test_expense_tracker.py -v
```

### 2. Run Main Program Demo
```bash
python main.py
```

### 3. Run Core Functionality Demo
```bash
python demo.py
```

### 4. Use in Code
```python
from expense_tracker import ExpenseTracker

# Create expense tracker
tracker = ExpenseTracker()

# Add expenses
tracker.add_expense("Lunch", 25.50, "Food")
tracker.add_expense("Transportation", 10.00, "Transportation")

# Calculate total expenses
total = tracker.calculate_total_expense()
print(f"Total expenses: ${total:.2f}")

# Display summary
tracker.display_summary()
```

## Test Coverage

Unit tests include the following test cases:
- Basic functionality tests for Expense class
- Negative amount validation tests
- All method tests for ExpenseTracker class
- Integration functionality tests
- Boundary condition tests

## Technical Features

- **Object-Oriented Design**: Uses classes and objects to organize code
- **Type Hints**: Uses Python type hints to improve code readability
- **Exception Handling**: Proper error handling for invalid inputs
- **Unit Testing**: Comprehensive test coverage ensures code quality
- **Documentation**: Detailed function and class documentation

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Example Output

```
=== Personal Expense Tracker ===
Welcome to the Personal Expense Tracking System!

1. Adding expense records:
Added expense: 2025-10-11 08:33 - Breakfast - $15.00 - Food
Added expense: 2025-10-11 08:33 - Lunch - $25.50 - Food
...

2. Calculating total expenses:
Total expense amount: $223.50

3. Expense summary:
=== Expense Summary ===
Total expense records: 6
Total expense amount: $223.50

By category:
  Food: 3 records, total $58.50
  Shopping: 1 records, total $120.00
  Transportation: 1 records, total $5.00
  Entertainment: 1 records, total $40.00
```
