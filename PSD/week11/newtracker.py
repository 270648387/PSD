import unittest

class ExpenseTracker:
    """A simple personal expense tracker."""
    def __init__(self):
        self.expenses = []  # store all amounts

    def add_expense(self, description, amount):
        """Add a new expense with description and amount."""
        self.expenses.append({"description": description, "amount": amount})

    def get_total(self):
        """Return the total of all expenses."""
        return sum(item["amount"] for item in self.expenses)

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. Show Total Expense")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            desc = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount! Try again.")
                continue
            tracker.add_expense(desc, amount)
            print(f"Added: {desc} - ${amount:.2f}")

        elif choice == "2":
            print(f"Total Expense: ${tracker.get_total():.2f}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


class TestExpenseTracker(unittest.TestCase):
    def test_add_and_total(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Breakfast", 15)
        tracker.add_expense("Grocery", 120)
        self.assertEqual(tracker.get_total(), 135)

    def test_empty_total(self):
        tracker = ExpenseTracker()
        self.assertEqual(tracker.get_total(), 0)

if __name__ == '__main__':
    unittest.main()
