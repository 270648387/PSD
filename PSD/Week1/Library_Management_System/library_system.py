from datetime import datetime, timedelta
from typing import List, Optional, Dict
from models import Book, Member, BorrowRecord, Fine, Genre

class LibrarySystem:
    """Main library management system that coordinates all operations"""
    
    def __init__(self, fine_rate_per_day: float = 1.0):
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}
        self.borrow_records: Dict[str, BorrowRecord] = {}
        self.fines: Dict[str, Fine] = {}
        self.fine_rate_per_day = fine_rate_per_day
    
    def add_book(self, book: Book) -> None:
        """Add a new book to the library"""
        self.books[book.get_book_id()] = book
        print(f"Book added: {book}")
    
    def remove_book(self, book_id: str) -> bool:
        """Remove a book from the library"""
        if book_id in self.books:
            book = self.books[book_id]
            if book.get_available_copies() == book.get_total_copies():
                del self.books[book_id]
                print(f"Book removed: {book}")
                return True
            else:
                print(f"Cannot remove book: {book.get_title()} - copies are currently borrowed")
                return False
        else:
            print(f"Book not found with ID: {book_id}")
            return False
    
    def update_book_information(self, book_id: str, **kwargs) -> bool:
        """Update book information"""
        if book_id in self.books:
            book = self.books[book_id]
            for key, value in kwargs.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            print(f"Book updated: {book}")
            return True
        else:
            print(f"Book not found with ID: {book_id}")
            return False
    
    def add_member(self, member: Member) -> None:
        """Add a new member to the library"""
        self.members[member.get_member_id()] = member
        print(f"Member added: {member}")
    
    def remove_member(self, member_id: str) -> bool:
        """Remove a member from the library"""
        if member_id in self.members:
            member = self.members[member_id]
            if member.get_current_books_borrowed() == 0:
                del self.members[member_id]
                print(f"Member removed: {member}")
                return True
            else:
                print(f"Cannot remove member: {member.get_name()} - has borrowed books")
                return False
        else:
            print(f"Member not found with ID: {member_id}")
            return False
    
    def borrow_book(self, book_id: str, member_id: str) -> Optional[BorrowRecord]:
        """Borrow a book for a member"""
        if book_id not in self.books:
            print(f"Book not found with ID: {book_id}")
            return None
        
        if member_id not in self.members:
            print(f"Member not found with ID: {member_id}")
            return None
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        # Check if member can borrow
        if not member.can_borrow_book():
            if member.get_current_books_borrowed() >= member.get_max_books_allowed():
                print(f"Member {member.get_name()} has reached the maximum borrowing limit")
            elif not member.is_membership_valid():
                print(f"Member {member.get_name()} has an expired membership")
            return None
        
        # Check if book is available
        if not book.is_available():
            print(f"Book '{book.get_title()}' is not available")
            return None
        
        # Create borrow record
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=14)  # 14 days loan period
        
        borrow_record = BorrowRecord(book_id, member_id, borrow_date, due_date)
        self.borrow_records[borrow_record.get_borrow_id()] = borrow_record
        
        # Update book and member
        book.decrease_available_copies()
        member.borrow_book()
        
        print(f"Book '{book.get_title()}' borrowed by {member.get_name()}")
        print(f"Due date: {due_date.strftime('%Y-%m-%d')}")
        
        return borrow_record
    
    def return_book(self, borrow_id: str) -> bool:
        """Return a borrowed book"""
        if borrow_id not in self.borrow_records:
            print(f"Borrow record not found with ID: {borrow_id}")
            return False
        
        borrow_record = self.borrow_records[borrow_id]
        
        if borrow_record.get_is_returned():
            print("Book has already been returned")
            return False
        
        # Get book and member
        book = self.books.get(borrow_record.get_book_id())
        member = self.members.get(borrow_record.get_member_id())
        
        if not book or not member:
            print("Book or member not found")
            return False
        
        # Return the book
        return_date = datetime.now()
        borrow_record.return_book(return_date)
        
        # Update book and member
        book.increase_available_copies()
        member.return_book()
        
        # Check for fines
        if borrow_record.get_fine_amount() > 0:
            fine = Fine(borrow_record.get_borrow_id(), 
                       borrow_record.get_member_id(), 
                       borrow_record.get_fine_amount())
            self.fines[fine.get_fine_id()] = fine
            
            print(f"Book '{book.get_title()}' returned by {member.get_name()}")
            print(f"Fine amount: ${borrow_record.get_fine_amount():.2f}")
        else:
            print(f"Book '{book.get_title()}' returned by {member.get_name()}")
            print("No fines applicable")
        
        return True
    
    def search_book(self, query: str) -> List[Book]:
        """Search books by title, author, or ISBN"""
        query = query.lower()
        results = []
        
        for book in self.books.values():
            if (query in book.get_title().lower() or 
                query in book.get_author().lower() or 
                query in book.get_isbn().lower()):
                results.append(book)
        
        return results
    
    def search_book_by_genre(self, genre: Genre) -> List[Book]:
        """Search books by genre"""
        results = []
        
        for book in self.books.values():
            if book.get_genre() == genre:
                results.append(book)
        
        return results
    
    def get_member_borrow_history(self, member_id: str) -> List[BorrowRecord]:
        """Get borrowing history for a member"""
        if member_id not in self.members:
            return []
        
        history = []
        for record in self.borrow_records.values():
            if record.get_member_id() == member_id:
                history.append(record)
        
        return sorted(history, key=lambda x: x.get_borrow_date(), reverse=True)
    
    def get_overdue_books(self) -> List[BorrowRecord]:
        """Get all overdue books"""
        overdue = []
        for record in self.borrow_records.values():
            if record.is_overdue() and not record.get_is_returned():
                overdue.append(record)
        
        return overdue
    
    def calculate_fine(self, borrow_record: BorrowRecord) -> float:
        """Calculate fine for a borrow record"""
        if borrow_record.get_is_returned():
            return borrow_record.get_fine_amount()
        
        if datetime.now() <= borrow_record.get_due_date():
            return 0.0
        
        overdue_days = (datetime.now() - borrow_record.get_due_date()).days
        return max(0, overdue_days * self.fine_rate_per_day)
    
    def process_fine_payment(self, fine_id: str, payment_date: datetime = None) -> bool:
        """Process payment for a fine"""
        if fine_id not in self.fines:
            print(f"Fine not found with ID: {fine_id}")
            return False
        
        fine = self.fines[fine_id]
        
        if fine.get_is_paid():
            print("Fine has already been paid")
            return False
        
        if payment_date is None:
            payment_date = datetime.now()
        
        fine.pay_fine(payment_date)
        print(f"Fine payment processed: ${fine.get_amount():.2f}")
        return True
    
    def extend_due_date(self, borrow_id: str, additional_days: int) -> bool:
        """Extend the due date for a borrowed book"""
        if borrow_id not in self.borrow_records:
            print(f"Borrow record not found with ID: {borrow_id}")
            return False
        
        borrow_record = self.borrow_records[borrow_id]
        
        if borrow_record.get_is_returned():
            print("Cannot extend due date for returned book")
            return False
        
        new_due_date = borrow_record.get_due_date() + timedelta(days=additional_days)
        borrow_record.due_date = new_due_date
        
        print(f"Due date extended to: {new_due_date.strftime('%Y-%m-%d')}")
        return True
    
    def generate_report(self) -> str:
        """Generate a comprehensive library report"""
        report = []
        report.append("=" * 50)
        report.append("LIBRARY MANAGEMENT SYSTEM REPORT")
        report.append("=" * 50)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Book statistics
        total_books = len(self.books)
        total_copies = sum(book.get_total_copies() for book in self.books.values())
        available_copies = sum(book.get_available_copies() for book in self.books.values())
        borrowed_copies = total_copies - available_copies
        
        report.append("BOOK STATISTICS:")
        report.append(f"  Total books: {total_books}")
        report.append(f"  Total copies: {total_copies}")
        report.append(f"  Available copies: {available_copies}")
        report.append(f"  Borrowed copies: {borrowed_copies}")
        report.append("")
        
        # Member statistics
        total_members = len(self.members)
        active_members = sum(1 for member in self.members.values() if member.is_membership_valid())
        expired_members = total_members - active_members
        
        report.append("MEMBER STATISTICS:")
        report.append(f"  Total members: {total_members}")
        report.append(f"  Active members: {active_members}")
        report.append(f"  Expired members: {expired_members}")
        report.append("")
        
        # Borrowing statistics
        total_borrows = len(self.borrow_records)
        active_borrows = sum(1 for record in self.borrow_records.values() if not record.get_is_returned())
        overdue_books = len(self.get_overdue_books())
        
        report.append("BORROWING STATISTICS:")
        report.append(f"  Total borrows: {total_borrows}")
        report.append(f"  Active borrows: {active_borrows}")
        report.append(f"  Overdue books: {overdue_books}")
        report.append("")
        
        # Fine statistics
        total_fines = len(self.fines)
        paid_fines = sum(1 for fine in self.fines.values() if fine.get_is_paid())
        unpaid_fines = total_fines - paid_fines
        total_fine_amount = sum(fine.get_amount() for fine in self.fines.values())
        
        report.append("FINE STATISTICS:")
        report.append(f"  Total fines: {total_fines}")
        report.append(f"  Paid fines: {paid_fines}")
        report.append(f"  Unpaid fines: {unpaid_fines}")
        report.append(f"  Total fine amount: ${total_fine_amount:.2f}")
        report.append("")
        
        report.append("=" * 50)
        
        return "\n".join(report)
    
    def get_book_by_id(self, book_id: str) -> Optional[Book]:
        """Get a book by its ID"""
        return self.books.get(book_id)
    
    def get_member_by_id(self, member_id: str) -> Optional[Member]:
        """Get a member by their ID"""
        return self.members.get(member_id)
    
    def get_borrow_record_by_id(self, borrow_id: str) -> Optional[BorrowRecord]:
        """Get a borrow record by its ID"""
        return self.borrow_records.get(borrow_id)
    
    def get_fine_by_id(self, fine_id: str) -> Optional[Fine]:
        """Get a fine by its ID"""
        return self.fines.get(fine_id)

