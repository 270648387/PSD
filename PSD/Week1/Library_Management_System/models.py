from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional
import uuid

class Genre(Enum):
    """Enum for book genres"""
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE = "Science"
    TECHNOLOGY = "Technology"
    HISTORY = "History"
    LITERATURE = "Literature"
    PHILOSOPHY = "Philosophy"
    ART = "Art"
    OTHER = "Other"

class Book:
    """Represents a book in the library system"""
    
    def __init__(self, title: str, author: str, isbn: str, publication_date: datetime, 
                 genre: Genre, total_copies: int = 1):
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def get_book_id(self) -> str:
        return self.book_id
    
    def get_title(self) -> str:
        return self.title
    
    def get_author(self) -> str:
        return self.author
    
    def get_isbn(self) -> str:
        return self.isbn
    
    def get_publication_date(self) -> datetime:
        return self.publication_date
    
    def get_genre(self) -> Genre:
        return self.genre
    
    def get_total_copies(self) -> int:
        return self.total_copies
    
    def get_available_copies(self) -> int:
        return self.available_copies
    
    def is_available(self) -> bool:
        return self.available_copies > 0
    
    def decrease_available_copies(self) -> None:
        if self.available_copies > 0:
            self.available_copies -= 1
    
    def increase_available_copies(self) -> None:
        if self.available_copies < self.total_copies:
            self.available_copies += 1
    
    def set_total_copies(self, total: int) -> None:
        if total >= 0:
            self.total_copies = total
            if self.available_copies > total:
                self.available_copies = total
    
    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author} ({self.genre.value})"

class Member:
    """Represents a library member"""
    
    def __init__(self, name: str, email: str, phone: str, address: str, 
                 membership_expiry_date: datetime):
        self.member_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.membership_expiry_date = membership_expiry_date
        self.max_books_allowed = 5
        self.current_books_borrowed = 0
    
    def get_member_id(self) -> str:
        return self.member_id
    
    def get_name(self) -> str:
        return self.name
    
    def get_email(self) -> str:
        return self.email
    
    def get_phone(self) -> str:
        return self.phone
    
    def get_address(self) -> str:
        return self.address
    
    def get_membership_expiry_date(self) -> datetime:
        return self.membership_expiry_date
    
    def get_max_books_allowed(self) -> int:
        return self.max_books_allowed
    
    def get_current_books_borrowed(self) -> int:
        return self.current_books_borrowed
    
    def can_borrow_book(self) -> bool:
        return (self.current_books_borrowed < self.max_books_allowed and 
                self.is_membership_valid())
    
    def borrow_book(self) -> None:
        if self.can_borrow_book():
            self.current_books_borrowed += 1
    
    def return_book(self) -> None:
        if self.current_books_borrowed > 0:
            self.current_books_borrowed -= 1
    
    def is_membership_valid(self) -> bool:
        return datetime.now() < self.membership_expiry_date
    
    def update_contact_info(self, email: str, phone: str, address: str) -> None:
        self.email = email
        self.phone = phone
        self.address = address
    
    def __str__(self) -> str:
        return f"Member: {self.name} (ID: {self.member_id})"

class BorrowRecord:
    """Represents a book borrowing transaction"""
    
    def __init__(self, book_id: str, member_id: str, borrow_date: datetime, due_date: datetime):
        self.borrow_id = str(uuid.uuid4())
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date: Optional[datetime] = None
        self.is_returned = False
        self.fine_amount = 0.0
    
    def get_borrow_id(self) -> str:
        return self.borrow_id
    
    def get_book_id(self) -> str:
        return self.book_id
    
    def get_member_id(self) -> str:
        return self.member_id
    
    def get_borrow_date(self) -> datetime:
        return self.borrow_date
    
    def get_due_date(self) -> datetime:
        return self.due_date
    
    def get_return_date(self) -> Optional[datetime]:
        return self.return_date
    
    def get_is_returned(self) -> bool:
        return self.is_returned
    
    def get_fine_amount(self) -> float:
        return self.fine_amount
    
    def return_book(self, return_date: datetime) -> None:
        self.return_date = return_date
        self.is_returned = True
        self.fine_amount = self.calculate_fine()
    
    def calculate_fine(self) -> float:
        if not self.is_returned or not self.return_date:
            return 0.0
        
        if self.return_date <= self.due_date:
            return 0.0
        
        overdue_days = (self.return_date - self.due_date).days
        return max(0, overdue_days * 1.0)  # $1.00 per day
    
    def is_overdue(self) -> bool:
        if self.is_returned:
            return self.return_date > self.due_date
        return datetime.now() > self.due_date
    
    def __str__(self) -> str:
        status = "Returned" if self.is_returned else "Borrowed"
        return f"Borrow Record: {self.borrow_id} - {status}"

class Fine:
    """Represents a fine for overdue books"""
    
    def __init__(self, borrow_record_id: str, member_id: str, amount: float):
        self.fine_id = str(uuid.uuid4())
        self.borrow_record_id = borrow_record_id
        self.member_id = member_id
        self.amount = amount
        self.due_date = datetime.now() + timedelta(days=30)  # 30 days to pay
        self.is_paid = False
        self.payment_date: Optional[datetime] = None
    
    def get_fine_id(self) -> str:
        return self.fine_id
    
    def get_borrow_record_id(self) -> str:
        return self.borrow_record_id
    
    def get_member_id(self) -> str:
        return self.member_id
    
    def get_amount(self) -> float:
        return self.amount
    
    def get_due_date(self) -> datetime:
        return self.due_date
    
    def get_is_paid(self) -> bool:
        return self.is_paid
    
    def get_payment_date(self) -> Optional[datetime]:
        return self.payment_date
    
    def pay_fine(self, payment_date: datetime) -> None:
        self.is_paid = True
        self.payment_date = payment_date
    
    def calculate_interest(self) -> float:
        if self.get_is_paid():
            return 0.0
        
        if datetime.now() > self.due_date:
            overdue_days = (datetime.now() - self.due_date).days
            return self.amount * 0.05 * overdue_days  # 5% interest per day overdue
        
        return 0.0
    
    def __str__(self) -> str:
        status = "Paid" if self.is_paid else "Unpaid"
        return f"Fine: ${self.amount:.2f} - {status}"

