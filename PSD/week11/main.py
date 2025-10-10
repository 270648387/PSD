"""
Personal Expense Tracker Main Program
Demonstrates how to use the ExpenseTracker class
"""

from expense_tracker import ExpenseTracker


def main():
    """Main program function"""
    print("=== Personal Expense Tracker ===")
    print("Welcome to the Personal Expense Tracking System!")
    
    # Create expense tracker instance
    tracker = ExpenseTracker()
    
    # Demonstrate adding expenses functionality
    print("\n1. Adding expense records:")
    tracker.add_expense("Breakfast", 15.00, "Food")
    tracker.add_expense("Lunch", 25.50, "Food")
    tracker.add_expense("Metro fare", 5.00, "Transportation")
    tracker.add_expense("Movie ticket", 40.00, "Entertainment")
    tracker.add_expense("Grocery shopping", 120.00, "Shopping")
    tracker.add_expense("Coffee", 18.00, "Food")
    
    # Demonstrate calculating total expenses functionality
    print(f"\n2. Calculating total expenses:")
    total = tracker.calculate_total_expense()
    print(f"Total expense amount: ${total:.2f}")
    
    # Display detailed summary
    print("\n3. Expense summary:")
    tracker.display_summary()
    
    # Demonstrate query by category
    print(f"\n4. Query by category:")
    print(f"Food category total: ${tracker.get_total_by_category('Food'):.2f}")
    print(f"Transportation category total: ${tracker.get_total_by_category('Transportation'):.2f}")
    print(f"Entertainment category total: ${tracker.get_total_by_category('Entertainment'):.2f}")
    print(f"Shopping category total: ${tracker.get_total_by_category('Shopping'):.2f}")
    
    # Demonstrate interactive functionality
    print(f"\n5. Interactive demo:")
    interactive_demo(tracker)


def interactive_demo(tracker):
    """Interactive demonstration functionality"""
    print("\n--- Interactive Demo ---")
    
    while True:
        print("\nPlease select an operation:")
        print("1. Add new expense")
        print("2. View total expenses")
        print("3. View all expenses")
        print("4. View expenses by category")
        print("5. Clear all records")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-5): ").strip()
        
        if choice == "0":
            print("Thank you for using the Personal Expense Tracker!")
            break
        elif choice == "1":
            add_expense_interactive(tracker)
        elif choice == "2":
            show_total_expense(tracker)
        elif choice == "3":
            show_all_expenses(tracker)
        elif choice == "4":
            show_expenses_by_category(tracker)
        elif choice == "5":
            clear_expenses(tracker)
        else:
            print("Invalid choice, please try again!")


def add_expense_interactive(tracker):
    """Interactive add expense"""
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            print("Expense description cannot be empty!")
            return
        
        amount_str = input("Enter expense amount: ").strip()
        amount = float(amount_str)
        
        category = input("Enter expense category (press Enter for default 'Other'): ").strip()
        if not category:
            category = "Other"
        
        tracker.add_expense(description, amount, category)
        
    except ValueError:
        print("Amount must be a valid number!")
    except Exception as e:
        print(f"Error adding expense: {e}")


def show_total_expense(tracker):
    """Display total expenses"""
    total = tracker.calculate_total_expense()
    count = tracker.get_expense_count()
    print(f"\nTotal expense records: {count}")
    print(f"Total expense amount: ${total:.2f}")


def show_all_expenses(tracker):
    """Display all expenses"""
    expenses = tracker.get_all_expenses()
    if not expenses:
        print("\nNo expense records found")
        return
    
    print(f"\nAll expense records (total {len(expenses)}):")
    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. {expense}")


def show_expenses_by_category(tracker):
    """Display expenses by category"""
    category = input("Enter category to query: ").strip()
    if not category:
        print("Category cannot be empty!")
        return
    
    expenses = tracker.get_expenses_by_category(category)
    total = tracker.get_total_by_category(category)
    
    if not expenses:
        print(f"\nNo expense records found for category '{category}'")
        return
    
    print(f"\nExpense records for category '{category}' (total {len(expenses)}):")
    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. {expense}")
    print(f"Total for this category: ${total:.2f}")


def clear_expenses(tracker):
    """Clear expense records"""
    confirm = input("Are you sure you want to clear all expense records? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        tracker.clear_all_expenses()
    else:
        print("Operation cancelled")


if __name__ == "__main__":
    main()
