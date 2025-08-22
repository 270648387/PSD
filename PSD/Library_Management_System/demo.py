#!/usr/bin/env python3
"""
Library Management System Demo
This script demonstrates all the functionality of the Library Management System
"""

from datetime import datetime, timedelta
from models import Book, Member, BorrowRecord, Fine, Genre
from library_system import LibrarySystem

def print_separator(title: str):
    """Print a formatted separator with title"""
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def demo_book_management(library: LibrarySystem):
    """Demonstrate book management functionality"""
    print_separator("BOOK MANAGEMENT DEMONSTRATION")
    
    # Add books
    print("1. Adding books to the library...")
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 
                 datetime(1925, 4, 10), Genre.FICTION, 3)
    book2 = Book("Python Programming", "John Smith", "978-1234567890", 
                 datetime(2020, 1, 15), Genre.TECHNOLOGY, 2)
    book3 = Book("History of Science", "Jane Doe", "978-0987654321", 
                 datetime(2018, 6, 20), Genre.SCIENCE, 1)
    book4 = Book("Art Through Ages", "Bob Wilson", "978-1122334455", 
                 datetime(2019, 3, 5), Genre.ART, 2)
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    
    # Search books
    print("\n2. Searching books...")
    search_results = library.search_book("Python")
    print(f"Search results for 'Python': {len(search_results)} books found")
    for book in search_results:
        print(f"  - {book}")
    
    # Search by genre
    print("\n3. Searching books by genre...")
    fiction_books = library.search_book_by_genre(Genre.FICTION)
    print(f"Fiction books: {len(fiction_books)} found")
    for book in fiction_books:
        print(f"  - {book}")
    
    # Update book information
    print("\n4. Updating book information...")
    library.update_book_information(book1.get_book_id(), total_copies=5)
    
    return [book1, book2, book3, book4]

def demo_member_management(library: LibrarySystem):
    """Demonstrate member management functionality"""
    print_separator("MEMBER MANAGEMENT DEMONSTRATION")
    
    # Add members
    print("1. Adding members to the library...")
    
    member1 = Member("Alice Johnson", "alice@email.com", "555-0101", 
                     "123 Main St, City", datetime.now() + timedelta(days=365))
    member2 = Member("Bob Smith", "bob@email.com", "555-0102", 
                     "456 Oak Ave, Town", datetime.now() + timedelta(days=180))
    member3 = Member("Carol Davis", "carol@email.com", "555-0103", 
                     "789 Pine Rd, Village", datetime.now() - timedelta(days=30))  # Expired
    
    library.add_member(member1)
    library.add_member(member2)
    library.add_member(member3)
    
    # Check member status
    print("\n2. Checking member status...")
    print(f"Alice can borrow: {member1.can_borrow_book()}")
    print(f"Bob can borrow: {member2.can_borrow_book()}")
    print(f"Carol can borrow: {member3.can_borrow_book()}")
    
    # Update contact information
    print("\n3. Updating member contact information...")
    member1.update_contact_info("alice.new@email.com", "555-0101", "123 Main St, New City")
    print(f"Alice's updated email: {member1.get_email()}")
    
    return [member1, member2, member3]

def demo_borrowing_process(library: LibrarySystem, books, members):
    """Demonstrate the borrowing process"""
    print_separator("BORROWING PROCESS DEMONSTRATION")
    
    # Borrow books
    print("1. Borrowing books...")
    
    # Alice borrows 2 books
    borrow1 = library.borrow_book(books[0].get_book_id(), members[0].get_member_id())
    borrow2 = library.borrow_book(books[1].get_book_id(), members[0].get_member_id())
    
    # Bob borrows 1 book
    borrow3 = library.borrow_book(books[2].get_book_id(), members[1].get_member_id())
    
    # Try to borrow more than limit
    print("\n2. Testing borrowing limits...")
    borrow4 = library.borrow_book(books[3].get_book_id(), members[0].get_member_id())
    
    # Check member status
    print(f"\nAlice's current borrowed books: {members[0].get_current_books_borrowed()}")
    print(f"Bob's current borrowed books: {members[1].get_current_books_borrowed()}")
    
    return [borrow1, borrow2, borrow3]

def demo_return_process(library: LibrarySystem, borrow_records, books, members):
    """Demonstrate the return process with fines"""
    print_separator("RETURN PROCESS DEMONSTRATION")
    
    # Simulate overdue return
    print("1. Simulating overdue return...")
    
    # Make the first book overdue by modifying the due date
    borrow_records[0].due_date = datetime.now() - timedelta(days=5)
    
    # Return the overdue book
    print("\n2. Returning overdue book...")
    library.return_book(borrow_records[0].get_borrow_id())
    
    # Return on-time book
    print("\n3. Returning on-time book...")
    library.return_book(borrow_records[1].get_borrow_id())
    
    # Check fines
    print("\n4. Checking fines...")
    overdue_records = library.get_overdue_books()
    print(f"Currently overdue books: {len(overdue_records)}")
    
    return borrow_records

def demo_fine_management(library: LibrarySystem):
    """Demonstrate fine management functionality"""
    print_separator("FINE MANAGEMENT DEMONSTRATION")
    
    # List all fines
    print("1. Current fines in the system:")
    fines = list(library.fines.values())
    if fines:
        for fine in fines:
            print(f"  - {fine}")
            print(f"    Amount: ${fine.get_amount():.2f}")
            print(f"    Due Date: {fine.get_due_date().strftime('%Y-%m-%d')}")
            print(f"    Status: {'Paid' if fine.get_is_paid() else 'Unpaid'}")
    else:
        print("  No fines currently in the system")
    
    # Process fine payment
    if fines:
        print("\n2. Processing fine payment...")
        library.process_fine_payment(fines[0].get_fine_id())
    
    # Check fine interest calculation
    if fines:
        print("\n3. Calculating fine interest...")
        interest = fines[0].calculate_interest()
        print(f"Interest on fine: ${interest:.2f}")

def demo_reporting(library: LibrarySystem):
    """Demonstrate reporting functionality"""
    print_separator("REPORTING DEMONSTRATION")
    
    # Generate comprehensive report
    print("Generating library report...")
    report = library.generate_report()
    print(report)

def demo_error_handling(library: LibrarySystem):
    """Demonstrate error handling"""
    print_separator("ERROR HANDLING DEMONSTRATION")
    
    print("1. Trying to borrow non-existent book...")
    library.borrow_book("non-existent-id", "non-existent-member")
    
    print("\n2. Trying to borrow book with non-existent member...")
    if library.books:
        first_book_id = list(library.books.keys())[0]
        library.borrow_book(first_book_id, "non-existent-member")
    
    print("\n3. Trying to return non-existent borrow record...")
    library.return_book("non-existent-borrow-id")
    
    print("\n4. Trying to remove member with borrowed books...")
    if library.members:
        first_member_id = list(library.members.keys())[0]
        library.remove_member(first_member_id)

def main():
    """Main demo function"""
    print("🏛️  LIBRARY MANAGEMENT SYSTEM DEMO 🏛️")
    print("This demo showcases all the functionality of the Library Management System")
    
    # Initialize library system
    library = LibrarySystem(fine_rate_per_day=1.0)
    
    try:
        # Run all demos
        books = demo_book_management(library)
        members = demo_member_management(library)
        borrow_records = demo_borrowing_process(library, books, members)
        demo_return_process(library, borrow_records, books, members)
        demo_fine_management(library)
        demo_reporting(library)
        demo_error_handling(library)
        
        print_separator("DEMO COMPLETED SUCCESSFULLY")
        print("✅ All functionality has been demonstrated!")
        print("📚 The Library Management System is working as expected.")
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
