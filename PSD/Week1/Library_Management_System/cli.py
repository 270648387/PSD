#!/usr/bin/env python3
"""
Library Management System - Command Line Interface
Interactive CLI for managing the library system
"""

import sys
from datetime import datetime, timedelta
from models import Book, Member, BorrowRecord, Fine, Genre
from library_system import LibrarySystem

class LibraryCLI:
    """Command Line Interface for the Library Management System"""
    
    def __init__(self):
        self.library = LibrarySystem()
        self.running = True
    
    def print_menu(self):
        """Print the main menu"""
        print("\n" + "=" * 60)
        print("🏛️  LIBRARY MANAGEMENT SYSTEM - MAIN MENU 🏛️")
        print("=" * 60)
        print("1.  Book Management")
        print("2.  Member Management")
        print("3.  Borrowing Operations")
        print("4.  Return Operations")
        print("5.  Fine Management")
        print("6.  Search & Reports")
        print("7.  Run Demo")
        print("0.  Exit")
        print("=" * 60)
    
    def book_management_menu(self):
        """Book management submenu"""
        while True:
            print("\n" + "-" * 40)
            print("📚 BOOK MANAGEMENT")
            print("-" * 40)
            print("1. Add new book")
            print("2. Remove book")
            print("3. Update book information")
            print("4. List all books")
            print("5. Search books")
            print("6. Search by genre")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-6): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.update_book()
            elif choice == "4":
                self.list_books()
            elif choice == "5":
                self.search_books()
            elif choice == "6":
                self.search_by_genre()
            else:
                print("❌ Invalid choice. Please try again.")
    
    def member_management_menu(self):
        """Member management submenu"""
        while True:
            print("\n" + "-" * 40)
            print("👥 MEMBER MANAGEMENT")
            print("-" * 40)
            print("1. Add new member")
            print("2. Remove member")
            print("3. Update member information")
            print("4. List all members")
            print("5. Check member status")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-5): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.add_member()
            elif choice == "2":
                self.remove_member()
            elif choice == "3":
                self.update_member()
            elif choice == "4":
                self.list_members()
            elif choice == "5":
                self.check_member_status()
            else:
                print("❌ Invalid choice. Please try again.")
    
    def borrowing_menu(self):
        """Borrowing operations submenu"""
        while True:
            print("\n" + "-" * 40)
            print("📖 BORROWING OPERATIONS")
            print("-" * 40)
            print("1. Borrow book")
            print("2. List active borrows")
            print("3. Extend due date")
            print("4. Check overdue books")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-4): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.borrow_book()
            elif choice == "2":
                self.list_active_borrows()
            elif choice == "3":
                self.extend_due_date()
            elif choice == "4":
                self.check_overdue_books()
            else:
                print("❌ Invalid choice. Please try again.")
    
    def return_menu(self):
        """Return operations submenu"""
        while True:
            print("\n" + "-" * 40)
            print("📚 RETURN OPERATIONS")
            print("-" * 40)
            print("1. Return book")
            print("2. View return history")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-2): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.return_book()
            elif choice == "2":
                self.view_return_history()
            else:
                print("❌ Invalid choice. Please try again.")
    
    def fine_menu(self):
        """Fine management submenu"""
        while True:
            print("\n" + "-" * 40)
            print("💰 FINE MANAGEMENT")
            print("-" * 40)
            print("1. View all fines")
            print("2. Process fine payment")
            print("3. Calculate fine interest")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-3): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.view_fines()
            elif choice == "2":
                self.process_fine_payment()
            elif choice == "3":
                self.calculate_fine_interest()
            else:
                print("❌ Invalid choice. Please try again.")
    
    def search_reports_menu(self):
        """Search and reports submenu"""
        while True:
            print("\n" + "-" * 40)
            print("🔍 SEARCH & REPORTS")
            print("-" * 40)
            print("1. Search books")
            print("2. Search by genre")
            print("3. Member borrowing history")
            print("4. Generate library report")
            print("0. Back to main menu")
            
            choice = input("\nEnter your choice (0-4): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.search_books()
            elif choice == "2":
                self.search_by_genre()
            elif choice == "3":
                self.member_borrowing_history()
            elif choice == "4":
                self.generate_report()
            else:
                print("❌ Invalid choice. Please try again.")
    
    def add_book(self):
        """Add a new book"""
        print("\n📚 ADD NEW BOOK")
        print("-" * 30)
        
        try:
            title = input("Enter book title: ").strip()
            if not title:
                print("❌ Title cannot be empty")
                return
            
            author = input("Enter author name: ").strip()
            if not author:
                print("❌ Author cannot be empty")
                return
            
            isbn = input("Enter ISBN: ").strip()
            if not isbn:
                print("❌ ISBN cannot be empty")
                return
            
            # Genre selection
            print("\nAvailable genres:")
            for i, genre in enumerate(Genre, 1):
                print(f"{i}. {genre.value}")
            
            genre_choice = input(f"Select genre (1-{len(Genre)}): ").strip()
            try:
                genre_index = int(genre_choice) - 1
                if 0 <= genre_index < len(Genre):
                    genre = list(Genre)[genre_index]
                else:
                    print("❌ Invalid genre selection")
                    return
            except ValueError:
                print("❌ Invalid genre selection")
                return
            
            # Publication date
            pub_date_str = input("Enter publication date (YYYY-MM-DD): ").strip()
            try:
                pub_date = datetime.strptime(pub_date_str, "%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD")
                return
            
            # Number of copies
            copies_str = input("Enter number of copies (default: 1): ").strip()
            copies = int(copies_str) if copies_str else 1
            
            if copies < 1:
                print("❌ Number of copies must be at least 1")
                return
            
            # Create and add book
            book = Book(title, author, isbn, pub_date, genre, copies)
            self.library.add_book(book)
            print(f"✅ Book '{title}' added successfully!")
            
        except Exception as e:
            print(f"❌ Error adding book: {e}")
    
    def add_member(self):
        """Add a new member"""
        print("\n👥 ADD NEW MEMBER")
        print("-" * 30)
        
        try:
            name = input("Enter member name: ").strip()
            if not name:
                print("❌ Name cannot be empty")
                return
            
            email = input("Enter email: ").strip()
            if not email:
                print("❌ Email cannot be empty")
                return
            
            phone = input("Enter phone number: ").strip()
            if not phone:
                print("❌ Phone cannot be empty")
                return
            
            address = input("Enter address: ").strip()
            if not address:
                print("❌ Address cannot be empty")
                return
            
            # Membership expiry
            expiry_str = input("Enter membership expiry date (YYYY-MM-DD): ").strip()
            try:
                expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD")
                return
            
            # Create and add member
            member = Member(name, email, phone, address, expiry_date)
            self.library.add_member(member)
            print(f"✅ Member '{name}' added successfully!")
            
        except Exception as e:
            print(f"❌ Error adding member: {e}")
    
    def borrow_book(self):
        """Borrow a book"""
        print("\n📖 BORROW BOOK")
        print("-" * 30)
        
        if not self.library.books:
            print("❌ No books available in the library")
            return
        
        if not self.library.members:
            print("❌ No members registered in the library")
            return
        
        try:
            # List available books
            print("Available books:")
            available_books = [book for book in self.library.books.values() if book.is_available()]
            if not available_books:
                print("❌ No books are currently available")
                return
            
            for i, book in enumerate(available_books, 1):
                print(f"{i}. {book.get_title()} by {book.get_author()} (Available: {book.get_available_copies()})")
            
            book_choice = input(f"Select book (1-{len(available_books)}): ").strip()
            try:
                book_index = int(book_choice) - 1
                if 0 <= book_index < len(available_books):
                    selected_book = available_books[book_index]
                else:
                    print("❌ Invalid book selection")
                    return
            except ValueError:
                print("❌ Invalid book selection")
                return
            
            # List members
            print("\nAvailable members:")
            for i, member in enumerate(self.library.members.values(), 1):
                status = "Active" if member.is_membership_valid() else "Expired"
                print(f"{i}. {member.get_name()} ({status}) - Borrowed: {member.get_current_books_borrowed()}/5")
            
            member_choice = input(f"Select member (1-{len(self.library.members)}): ").strip()
            try:
                member_index = int(member_choice) - 1
                if 0 <= member_index < len(self.library.members):
                    selected_member = list(self.library.members.values())[member_index]
                else:
                    print("❌ Invalid member selection")
                    return
            except ValueError:
                print("❌ Invalid member selection")
                return
            
            # Attempt to borrow
            borrow_record = self.library.borrow_book(selected_book.get_book_id(), selected_member.get_member_id())
            if borrow_record:
                print("✅ Book borrowed successfully!")
            else:
                print("❌ Failed to borrow book")
            
        except Exception as e:
            print(f"❌ Error borrowing book: {e}")
    
    def return_book(self):
        """Return a book"""
        print("\n📚 RETURN BOOK")
        print("-" * 30)
        
        # Get active borrows
        active_borrows = [record for record in self.library.borrow_records.values() if not record.get_is_returned()]
        
        if not active_borrows:
            print("❌ No active borrows to return")
            return
        
        try:
            print("Active borrows:")
            for i, record in enumerate(active_borrows, 1):
                book = self.library.get_book_by_id(record.get_book_id())
                member = self.library.get_member_by_id(record.get_member_id())
                due_date = record.get_due_date()
                overdue = record.is_overdue()
                
                if book and member:
                    status = "OVERDUE" if overdue else "On time"
                    print(f"{i}. {book.get_title()} borrowed by {member.get_name()}")
                    print(f"   Due: {due_date.strftime('%Y-%m-%d')} - {status}")
            
            choice = input(f"Select borrow to return (1-{len(active_borrows)}): ").strip()
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(active_borrows):
                    selected_record = active_borrows[choice_index]
                else:
                    print("❌ Invalid selection")
                    return
            except ValueError:
                print("❌ Invalid selection")
                return
            
            # Return the book
            if self.library.return_book(selected_record.get_borrow_id()):
                print("✅ Book returned successfully!")
            else:
                print("❌ Failed to return book")
            
        except Exception as e:
            print(f"❌ Error returning book: {e}")
    
    def list_books(self):
        """List all books"""
        print("\n📚 ALL BOOKS IN LIBRARY")
        print("-" * 40)
        
        if not self.library.books:
            print("No books in the library")
            return
        
        for i, book in enumerate(self.library.books.values(), 1):
            print(f"{i}. {book.get_title()} by {book.get_author()}")
            print(f"   Genre: {book.get_genre().value}")
            print(f"   ISBN: {book.get_isbn()}")
            print(f"   Copies: {book.get_available_copies()}/{book.get_total_copies()}")
            print(f"   Available: {'Yes' if book.is_available() else 'No'}")
            print()
    
    def list_members(self):
        """List all members"""
        print("\n👥 ALL MEMBERS")
        print("-" * 30)
        
        if not self.library.members:
            print("No members registered")
            return
        
        for i, member in enumerate(self.library.members.values(), 1):
            status = "Active" if member.is_membership_valid() else "Expired"
            print(f"{i}. {member.get_name()}")
            print(f"   Email: {member.get_email()}")
            print(f"   Phone: {member.get_phone()}")
            print(f"   Status: {status}")
            print(f"   Borrowed: {member.get_current_books_borrowed()}/5")
            print()
    
    def search_books(self):
        """Search books"""
        print("\n🔍 SEARCH BOOKS")
        print("-" * 30)
        
        query = input("Enter search term (title, author, or ISBN): ").strip()
        if not query:
            print("❌ Search term cannot be empty")
            return
        
        results = self.library.search_book(query)
        
        if results:
            print(f"\nFound {len(results)} book(s):")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book.get_title()} by {book.get_author()}")
                print(f"   Genre: {book.get_genre().value}")
                print(f"   Available: {'Yes' if book.is_available() else 'No'}")
                print()
        else:
            print("❌ No books found matching your search")
    
    def search_by_genre(self):
        """Search books by genre"""
        print("\n🔍 SEARCH BY GENRE")
        print("-" * 30)
        
        print("Available genres:")
        for i, genre in enumerate(Genre, 1):
            print(f"{i}. {genre.value}")
        
        choice = input(f"Select genre (1-{len(Genre)}): ").strip()
        try:
            genre_index = int(choice) - 1
            if 0 <= genre_index < len(Genre):
                selected_genre = list(Genre)[genre_index]
            else:
                print("❌ Invalid genre selection")
                return
        except ValueError:
            print("❌ Invalid genre selection")
            return
        
        results = self.library.search_book_by_genre(selected_genre)
        
        if results:
            print(f"\nFound {len(results)} book(s) in {selected_genre.value}:")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book.get_title()} by {book.get_author()}")
                print(f"   Available: {'Yes' if book.is_available() else 'No'}")
                print()
        else:
            print(f"❌ No books found in {selected_genre.value} genre")
    
    def generate_report(self):
        """Generate library report"""
        print("\n📊 LIBRARY REPORT")
        print("-" * 30)
        
        report = self.library.generate_report()
        print(report)
    
    def remove_book(self):
        """Remove a book"""
        print("\n📚 REMOVE BOOK")
        print("-" * 30)
        
        if not self.library.books:
            print("❌ No books in the library")
            return
        
        self.list_books()
        try:
            choice = input(f"Select book to remove (1-{len(self.library.books)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.books):
                book_id = list(self.library.books.keys())[choice_index]
                if self.library.remove_book(book_id):
                    print("✅ Book removed successfully!")
                else:
                    print("❌ Failed to remove book")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def update_book(self):
        """Update book information"""
        print("\n📚 UPDATE BOOK")
        print("-" * 30)
        
        if not self.library.books:
            print("❌ No books in the library")
            return
        
        self.list_books()
        try:
            choice = input(f"Select book to update (1-{len(self.library.books)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.books):
                book_id = list(self.library.books.keys())[choice_index]
                book = self.library.books[book_id]
                
                print(f"\nUpdating: {book.get_title()}")
                new_title = input("New title (or press Enter to keep current): ").strip()
                if new_title:
                    book.title = new_title
                
                new_author = input("New author (or press Enter to keep current): ").strip()
                if new_author:
                    book.author = new_author
                
                new_copies = input("New number of copies (or press Enter to keep current): ").strip()
                if new_copies:
                    try:
                        copies = int(new_copies)
                        if copies >= 0:
                            book.set_total_copies(copies)
                        else:
                            print("❌ Number of copies must be non-negative")
                    except ValueError:
                        print("❌ Invalid number format")
                
                print("✅ Book updated successfully!")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def remove_member(self):
        """Remove a member"""
        print("\n👥 REMOVE MEMBER")
        print("-" * 30)
        
        if not self.library.members:
            print("❌ No members registered")
            return
        
        self.list_members()
        try:
            choice = input(f"Select member to remove (1-{len(self.library.members)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.members):
                member_id = list(self.library.members.keys())[choice_index]
                if self.library.remove_member(member_id):
                    print("✅ Member removed successfully!")
                else:
                    print("❌ Failed to remove member")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def update_member(self):
        """Update member information"""
        print("\n👥 UPDATE MEMBER")
        print("-" * 30)
        
        if not self.library.members:
            print("❌ No members registered")
            return
        
        self.list_members()
        try:
            choice = input(f"Select member to update (1-{len(self.library.members)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.members):
                member_id = list(self.library.members.keys())[choice_index]
                member = self.library.members[member_id]
                
                print(f"\nUpdating: {member.get_name()}")
                new_email = input("New email (or press Enter to keep current): ").strip()
                if new_email:
                    member.email = new_email
                
                new_phone = input("New phone (or press Enter to keep current): ").strip()
                if new_phone:
                    member.phone = new_phone
                
                new_address = input("New address (or press Enter to keep current): ").strip()
                if new_address:
                    member.address = new_address
                
                print("✅ Member updated successfully!")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def check_member_status(self):
        """Check member status"""
        print("\n👥 CHECK MEMBER STATUS")
        print("-" * 30)
        
        if not self.library.members:
            print("❌ No members registered")
            return
        
        self.list_members()
        try:
            choice = input(f"Select member to check (1-{len(self.library.members)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.members):
                member = list(self.library.members.values())[choice_index]
                print(f"\nMember: {member.get_name()}")
                print(f"Email: {member.get_email()}")
                print(f"Phone: {member.get_phone()}")
                print(f"Address: {member.get_address()}")
                print(f"Membership expires: {member.get_membership_expiry_date().strftime('%Y-%m-%d')}")
                print(f"Membership valid: {'Yes' if member.is_membership_valid() else 'No'}")
                print(f"Books borrowed: {member.get_current_books_borrowed()}/{member.get_max_books_allowed()}")
                print(f"Can borrow: {'Yes' if member.can_borrow_book() else 'No'}")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def list_active_borrows(self):
        """List active borrows"""
        print("\n📖 ACTIVE BORROWS")
        print("-" * 30)
        
        active_borrows = [record for record in self.library.borrow_records.values() if not record.get_is_returned()]
        
        if not active_borrows:
            print("No active borrows")
            return
        
        for i, record in enumerate(active_borrows, 1):
            book = self.library.get_book_by_id(record.get_book_id())
            member = self.library.get_member_by_id(record.get_member_id())
            due_date = record.get_due_date()
            overdue = record.is_overdue()
            
            if book and member:
                status = "OVERDUE" if overdue else "On time"
                print(f"{i}. {book.get_title()} borrowed by {member.get_name()}")
                print(f"   Due: {due_date.strftime('%Y-%m-%d')} - {status}")
                print()
    
    def extend_due_date(self):
        """Extend due date"""
        print("\n📅 EXTEND DUE DATE")
        print("-" * 30)
        
        active_borrows = [record for record in self.library.borrow_records.values() if not record.get_is_returned()]
        
        if not active_borrows:
            print("❌ No active borrows to extend")
            return
        
        self.list_active_borrows()
        try:
            choice = input(f"Select borrow to extend (1-{len(active_borrows)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(active_borrows):
                selected_record = active_borrows[choice_index]
                days_str = input("Enter additional days: ").strip()
                try:
                    days = int(days_str)
                    if days > 0:
                        if self.library.extend_due_date(selected_record.get_borrow_id(), days):
                            print("✅ Due date extended successfully!")
                        else:
                            print("❌ Failed to extend due date")
                    else:
                        print("❌ Days must be positive")
                except ValueError:
                    print("❌ Invalid number format")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def check_overdue_books(self):
        """Check overdue books"""
        print("\n⏰ OVERDUE BOOKS")
        print("-" * 30)
        
        overdue_records = self.library.get_overdue_books()
        
        if not overdue_records:
            print("No overdue books")
            return
        
        for i, record in enumerate(overdue_records, 1):
            book = self.library.get_book_by_id(record.get_book_id())
            member = self.library.get_member_by_id(record.get_member_id())
            due_date = record.get_due_date()
            fine = self.library.calculate_fine(record)
            
            if book and member:
                print(f"{i}. {book.get_title()} borrowed by {member.get_name()}")
                print(f"   Due: {due_date.strftime('%Y-%m-%d')}")
                print(f"   Fine: ${fine:.2f}")
                print()
    
    def view_return_history(self):
        """View return history"""
        print("\n📚 RETURN HISTORY")
        print("-" * 30)
        
        returned_records = [record for record in self.library.borrow_records.values() if record.get_is_returned()]
        
        if not returned_records:
            print("No returned books")
            return
        
        for i, record in enumerate(returned_records, 1):
            book = self.library.get_book_by_id(record.get_book_id())
            member = self.library.get_member_by_id(record.get_member_id())
            return_date = record.get_return_date()
            fine = record.get_fine_amount()
            
            if book and member:
                print(f"{i}. {book.get_title()} returned by {member.get_name()}")
                print(f"   Returned: {return_date.strftime('%Y-%m-%d')}")
                if fine > 0:
                    print(f"   Fine: ${fine:.2f}")
                print()
    
    def view_fines(self):
        """View all fines"""
        print("\n💰 ALL FINES")
        print("-" * 30)
        
        if not self.library.fines:
            print("No fines in the system")
            return
        
        for i, fine in enumerate(self.library.fines.values(), 1):
            member = self.library.get_member_by_id(fine.get_member_id())
            member_name = member.get_name() if member else "Unknown"
            
            print(f"{i}. Fine ID: {fine.get_fine_id()}")
            print(f"   Member: {member_name}")
            print(f"   Amount: ${fine.get_amount():.2f}")
            print(f"   Due Date: {fine.get_due_date().strftime('%Y-%m-%d')}")
            print(f"   Status: {'Paid' if fine.get_is_paid() else 'Unpaid'}")
            if fine.get_is_paid() and fine.get_payment_date():
                print(f"   Paid: {fine.get_payment_date().strftime('%Y-%m-%d')}")
            print()
    
    def process_fine_payment(self):
        """Process fine payment"""
        print("\n💰 PROCESS FINE PAYMENT")
        print("-" * 30)
        
        unpaid_fines = [fine for fine in self.library.fines.values() if not fine.get_is_paid()]
        
        if not unpaid_fines:
            print("❌ No unpaid fines")
            return
        
        self.view_fines()
        try:
            choice = input(f"Select fine to pay (1-{len(unpaid_fines)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(unpaid_fines):
                selected_fine = unpaid_fines[choice_index]
                if self.library.process_fine_payment(selected_fine.get_fine_id()):
                    print("✅ Fine payment processed successfully!")
                else:
                    print("❌ Failed to process fine payment")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def calculate_fine_interest(self):
        """Calculate fine interest"""
        print("\n💰 CALCULATE FINE INTEREST")
        print("-" * 30)
        
        if not self.library.fines:
            print("❌ No fines in the system")
            return
        
        self.view_fines()
        try:
            choice = input(f"Select fine to calculate interest (1-{len(self.library.fines)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.fines):
                selected_fine = list(self.library.fines.values())[choice_index]
                interest = selected_fine.calculate_interest()
                print(f"Interest on fine: ${interest:.2f}")
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def member_borrowing_history(self):
        """View member borrowing history"""
        print("\n📚 MEMBER BORROWING HISTORY")
        print("-" * 30)
        
        if not self.library.members:
            print("❌ No members registered")
            return
        
        self.list_members()
        try:
            choice = input(f"Select member to view history (1-{len(self.library.members)}): ").strip()
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(self.library.members):
                selected_member = list(self.library.members.values())[choice_index]
                history = self.library.get_member_borrow_history(selected_member.get_member_id())
                
                if not history:
                    print(f"\nNo borrowing history for {selected_member.get_name()}")
                    return
                
                print(f"\nBorrowing history for {selected_member.get_name()}:")
                for i, record in enumerate(history, 1):
                    book = self.library.get_book_by_id(record.get_book_id())
                    if book:
                        status = "Returned" if record.get_is_returned() else "Borrowed"
                        print(f"{i}. {book.get_title()}")
                        print(f"   Borrowed: {record.get_borrow_date().strftime('%Y-%m-%d')}")
                        print(f"   Due: {record.get_due_date().strftime('%Y-%m-%d')}")
                        print(f"   Status: {status}")
                        if record.get_is_returned() and record.get_return_date():
                            print(f"   Returned: {record.get_return_date().strftime('%Y-%m-%d')}")
                        if record.get_fine_amount() > 0:
                            print(f"   Fine: ${record.get_fine_amount():.2f}")
                        print()
            else:
                print("❌ Invalid selection")
        except (ValueError, IndexError):
            print("❌ Invalid selection")
    
    def run_demo(self):
        """Run the demo script"""
        print("\n🎬 RUNNING DEMO...")
        print("-" * 30)
        
        try:
            from demo import main
            main()
        except ImportError:
            print("❌ Demo module not found")
        except Exception as e:
            print(f"❌ Error running demo: {e}")
    
    def run(self):
        """Main CLI loop"""
        print("🏛️  Welcome to the Library Management System!")
        print("This is an interactive command-line interface for managing your library.")
        
        while self.running:
            try:
                self.print_menu()
                choice = input("\nEnter your choice (0-7): ").strip()
                
                if choice == "0":
                    print("\n👋 Thank you for using the Library Management System!")
                    self.running = False
                elif choice == "1":
                    self.book_management_menu()
                elif choice == "2":
                    self.member_management_menu()
                elif choice == "3":
                    self.borrowing_menu()
                elif choice == "4":
                    self.return_menu()
                elif choice == "5":
                    self.fine_menu()
                elif choice == "6":
                    self.search_reports_menu()
                elif choice == "7":
                    self.run_demo()
                else:
                    print("❌ Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                self.running = False
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                import traceback
                traceback.print_exc()

def main():
    """Main function"""
    cli = LibraryCLI()
    cli.run()

if __name__ == "__main__":
    main()
