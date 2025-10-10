"""
Unit tests for Personal Expense Tracker
"""

import unittest
from datetime import datetime
from expense_tracker import Expense, ExpenseTracker


class TestExpense(unittest.TestCase):
    """Test Expense class"""
    
    def test_expense_creation(self):
        """Test expense record creation"""
        expense = Expense("Lunch", 25.50, "Food")
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.amount, 25.50)
        self.assertEqual(expense.category, "Food")
        self.assertIsInstance(expense.date, datetime)
    
    def test_expense_creation_with_default_category(self):
        """Test expense record creation with default category"""
        expense = Expense("Transportation", 10.00)
        self.assertEqual(expense.description, "Transportation")
        self.assertEqual(expense.amount, 10.00)
        self.assertEqual(expense.category, "Other")
    
    def test_negative_amount_raises_error(self):
        """Test that negative amount should raise exception"""
        with self.assertRaises(ValueError):
            Expense("Test", -10.00)
    
    def test_expense_string_representation(self):
        """Test expense record string representation"""
        expense = Expense("Test expense", 100.00, "Test")
        str_repr = str(expense)
        self.assertIn("Test expense", str_repr)
        self.assertIn("100.00", str_repr)
        self.assertIn("Test", str_repr)


class TestExpenseTracker(unittest.TestCase):
    """Test ExpenseTracker class"""
    
    def setUp(self):
        """Setup before each test"""
        self.tracker = ExpenseTracker()
    
    def test_initial_state(self):
        """Test initial state"""
        self.assertEqual(len(self.tracker.expenses), 0)
        self.assertEqual(self.tracker.calculate_total_expense(), 0.0)
        self.assertEqual(self.tracker.get_expense_count(), 0)
    
    def test_add_single_expense(self):
        """Test adding single expense"""
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.assertEqual(self.tracker.get_expense_count(), 1)
        self.assertEqual(self.tracker.calculate_total_expense(), 25.50)
    
    def test_add_multiple_expenses(self):
        """Test adding multiple expenses"""
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.tracker.add_expense("Transportation", 10.00, "Transportation")
        self.tracker.add_expense("Movie ticket", 35.00, "Entertainment")
        
        self.assertEqual(self.tracker.get_expense_count(), 3)
        self.assertEqual(self.tracker.calculate_total_expense(), 70.50)
    
    def test_calculate_total_expense_empty(self):
        """Test total expense calculation for empty list"""
        self.assertEqual(self.tracker.calculate_total_expense(), 0.0)
    
    def test_get_expenses_by_category(self):
        """Test getting expenses by category"""
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.tracker.add_expense("Dinner", 30.00, "Food")
        self.tracker.add_expense("Transportation", 10.00, "Transportation")
        
        food_expenses = self.tracker.get_expenses_by_category("Food")
        self.assertEqual(len(food_expenses), 2)
        
        transport_expenses = self.tracker.get_expenses_by_category("Transportation")
        self.assertEqual(len(transport_expenses), 1)
        
        other_expenses = self.tracker.get_expenses_by_category("Other")
        self.assertEqual(len(other_expenses), 0)
    
    def test_get_total_by_category(self):
        """Test calculating total expenses by category"""
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.tracker.add_expense("Dinner", 30.00, "Food")
        self.tracker.add_expense("Transportation", 10.00, "Transportation")
        
        food_total = self.tracker.get_total_by_category("Food")
        self.assertEqual(food_total, 55.50)
        
        transport_total = self.tracker.get_total_by_category("Transportation")
        self.assertEqual(transport_total, 10.00)
        
        other_total = self.tracker.get_total_by_category("Other")
        self.assertEqual(other_total, 0.0)
    
    def test_get_all_expenses(self):
        """Test getting all expense records"""
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.tracker.add_expense("Transportation", 10.00, "Transportation")
        
        all_expenses = self.tracker.get_all_expenses()
        self.assertEqual(len(all_expenses), 2)
        self.assertIsInstance(all_expenses[0], Expense)
        self.assertIsInstance(all_expenses[1], Expense)
    
    def test_clear_all_expenses(self):
        """Test clearing all expense records"""
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.tracker.add_expense("Transportation", 10.00, "Transportation")
        
        self.assertEqual(self.tracker.get_expense_count(), 2)
        
        self.tracker.clear_all_expenses()
        self.assertEqual(self.tracker.get_expense_count(), 0)
        self.assertEqual(self.tracker.calculate_total_expense(), 0.0)
    
    def test_add_expense_with_negative_amount(self):
        """Test that adding expense with negative amount should raise exception"""
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Test", -10.00)
    
    def test_expense_tracker_integration(self):
        """Test expense tracker integration functionality"""
        # Add various types of expenses
        self.tracker.add_expense("Breakfast", 15.00, "Food")
        self.tracker.add_expense("Lunch", 25.50, "Food")
        self.tracker.add_expense("Metro", 5.00, "Transportation")
        self.tracker.add_expense("Movie", 40.00, "Entertainment")
        self.tracker.add_expense("Shopping", 120.00, "Shopping")
        
        # Verify total expenses
        total = self.tracker.calculate_total_expense()
        expected_total = 15.00 + 25.50 + 5.00 + 40.00 + 120.00
        self.assertEqual(total, expected_total)
        
        # Verify record count
        self.assertEqual(self.tracker.get_expense_count(), 5)
        
        # Verify statistics by category
        food_total = self.tracker.get_total_by_category("Food")
        self.assertEqual(food_total, 40.50)
        
        transport_total = self.tracker.get_total_by_category("Transportation")
        self.assertEqual(transport_total, 5.00)
        
        entertainment_total = self.tracker.get_total_by_category("Entertainment")
        self.assertEqual(entertainment_total, 40.00)
        
        shopping_total = self.tracker.get_total_by_category("Shopping")
        self.assertEqual(shopping_total, 120.00)


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
