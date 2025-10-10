"""
Personal Expense Tracker - Object-Oriented Programming Implementation
"""

from datetime import datetime
from typing import List, Optional


class Expense:
    """Class representing a single expense record"""
    
    def __init__(self, description: str, amount: float, category: str = "Other"):
        """
        Initialize expense record
        
        Args:
            description (str): Expense description
            amount (float): Expense amount
            category (str): Expense category, defaults to "Other"
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative")
        
        self.description = description
        self.amount = amount
        self.category = category
        self.date = datetime.now()
    
    def __str__(self) -> str:
        """Return string representation of expense record"""
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} - {self.description} - ${self.amount:.2f} - {self.category}"
    
    def __repr__(self) -> str:
        """Return detailed representation of expense record"""
        return f"Expense(description='{self.description}', amount={self.amount}, category='{self.category}')"


class ExpenseTracker:
    """Main class for personal expense tracking"""
    
    def __init__(self):
        """Initialize expense tracker"""
        self.expenses: List[Expense] = []
    
    def add_expense(self, description: str, amount: float, category: str = "Other") -> None:
        """
        Add new expense record
        
        Args:
            description (str): Expense description
            amount (float): Expense amount
            category (str): Expense category
        """
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        print(f"Added expense: {expense}")
    
    def calculate_total_expense(self) -> float:
        """
        Calculate total amount of all expenses
        
        Returns:
            float: Total expense amount
        """
        return sum(expense.amount for expense in self.expenses)
    
    def get_expenses_by_category(self, category: str) -> List[Expense]:
        """
        Get expense records by category
        
        Args:
            category (str): Expense category
            
        Returns:
            List[Expense]: List of expense records in this category
        """
        return [expense for expense in self.expenses if expense.category == category]
    
    def get_total_by_category(self, category: str) -> float:
        """
        Calculate total expenses for specific category
        
        Args:
            category (str): Expense category
            
        Returns:
            float: Total expense amount for this category
        """
        return sum(expense.amount for expense in self.get_expenses_by_category(category))
    
    def get_all_expenses(self) -> List[Expense]:
        """
        Get all expense records
        
        Returns:
            List[Expense]: List of all expense records
        """
        return self.expenses.copy()
    
    def get_expense_count(self) -> int:
        """
        Get total number of expense records
        
        Returns:
            int: Number of expense records
        """
        return len(self.expenses)
    
    def clear_all_expenses(self) -> None:
        """Clear all expense records"""
        self.expenses.clear()
        print("All expenses cleared")
    
    def display_summary(self) -> None:
        """Display expense summary"""
        if not self.expenses:
            print("No expense records found")
            return
        
        print("\n=== Expense Summary ===")
        print(f"Total expense records: {self.get_expense_count()}")
        print(f"Total expense amount: ${self.calculate_total_expense():.2f}")
        
        # Display expenses by category
        categories = set(expense.category for expense in self.expenses)
        print("\nBy category:")
        for category in categories:
            total = self.get_total_by_category(category)
            count = len(self.get_expenses_by_category(category))
            print(f"  {category}: {count} records, total ${total:.2f}")
        
        print("\nAll expense records:")
        for i, expense in enumerate(self.expenses, 1):
            print(f"  {i}. {expense}")
