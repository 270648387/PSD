"""
Personal Expense Tracker Demo Script
Demonstrates core functionality: Add expenses and calculate total expenses
"""

from expense_tracker import ExpenseTracker


def demo_core_functions():
    """Demonstrate core functionality"""
    print("=== Personal Expense Tracker Core Functionality Demo ===\n")
    
    # Create expense tracker
    tracker = ExpenseTracker()
    
    # Demonstrate adding expenses functionality
    print("1. Adding expense records:")
    print("-" * 30)
    
    expenses_data = [
        ("Breakfast", 15.00, "Food"),
        ("Lunch", 25.50, "Food"),
        ("Metro fare", 5.00, "Transportation"),
        ("Movie ticket", 40.00, "Entertainment"),
        ("Grocery shopping", 120.00, "Shopping"),
        ("Coffee", 18.00, "Food")
    ]
    
    for description, amount, category in expenses_data:
        tracker.add_expense(description, amount, category)
    
    print(f"\n2. Calculating total expenses:")
    print("-" * 30)
    total = tracker.calculate_total_expense()
    print(f"Total expense amount: ${total:.2f}")
    print(f"Number of expense records: {tracker.get_expense_count()}")
    
    print(f"\n3. Statistics by category:")
    print("-" * 30)
    categories = set(expense.category for expense in tracker.get_all_expenses())
    for category in categories:
        category_total = tracker.get_total_by_category(category)
        category_count = len(tracker.get_expenses_by_category(category))
        print(f"{category}: {category_count} records, total ${category_total:.2f}")
    
    print(f"\n4. All expense records:")
    print("-" * 30)
    for i, expense in enumerate(tracker.get_all_expenses(), 1):
        print(f"{i}. {expense}")


if __name__ == "__main__":
    demo_core_functions()
