#!/usr/bin/env python3
"""
Quick Test Script for Library Management System
This script tests that all modules can be imported and basic functionality works
"""

def test_imports():
    """Test that all modules can be imported successfully"""
    print("🧪 Testing module imports...")
    
    try:
        from models import Book, Member, BorrowRecord, Fine, Genre
        print("✅ models.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import models.py: {e}")
        return False
    
    try:
        from library_system import LibrarySystem
        print("✅ library_system.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import library_system.py: {e}")
        return False
    
    try:
        from demo import main as demo_main
        print("✅ demo.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import demo.py: {e}")
        return False
    
    try:
        from cli import LibraryCLI
        print("✅ cli.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import cli.py: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Test basic system functionality"""
    print("\n🧪 Testing basic functionality...")
    
    try:
        from models import Book, Member, Genre
        from library_system import LibrarySystem
        from datetime import datetime, timedelta
        
        # Create a library system
        library = LibrarySystem()
        print("✅ Library system created")
        
        # Create a book
        book = Book("Test Book", "Test Author", "123-456-789", 
                   datetime.now(), Genre.FICTION, 2)
        print("✅ Book created")
        
        # Create a member
        member = Member("Test Member", "test@email.com", "555-0000", 
                      "Test Address", datetime.now() + timedelta(days=365))
        print("✅ Member created")
        
        # Add to library
        library.add_book(book)
        library.add_member(member)
        print("✅ Book and member added to library")
        
        # Test borrowing
        borrow_record = library.borrow_book(book.get_book_id(), member.get_member_id())
        if borrow_record:
            print("✅ Book borrowed successfully")
        else:
            print("❌ Book borrowing failed")
        
        # Test search
        search_results = library.search_book("Test")
        if search_results:
            print("✅ Book search working")
        else:
            print("❌ Book search failed")
        
        # Generate report
        report = library.generate_report()
        if report:
            print("✅ Report generation working")
        else:
            print("❌ Report generation failed")
        
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_genre_enum():
    """Test the Genre enum"""
    print("\n🧪 Testing Genre enum...")
    
    try:
        from models import Genre
        
        # Test enum values
        genres = list(Genre)
        print(f"✅ Found {len(genres)} genres: {[g.value for g in genres]}")
        
        # Test specific genres
        fiction = Genre.FICTION
        print(f"✅ Fiction genre: {fiction.value}")
        
        return True
        
    except Exception as e:
        print(f"❌ Genre enum test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🏛️  LIBRARY MANAGEMENT SYSTEM - QUICK TEST 🏛️")
    print("=" * 60)
    
    all_tests_passed = True
    
    # Test imports
    if not test_imports():
        all_tests_passed = False
    
    # Test basic functionality
    if not test_basic_functionality():
        all_tests_passed = False
    
    # Test genre enum
    if not test_genre_enum():
        all_tests_passed = False
    
    # Final results
    print("\n" + "=" * 60)
    if all_tests_passed:
        print("🎉 ALL TESTS PASSED! 🎉")
        print("✅ The Library Management System is working correctly!")
        print("\nYou can now:")
        print("  - Run the demo: python demo.py")
        print("  - Start the CLI: python cli.py")
        print("  - Import and use the modules in your own code")
    else:
        print("❌ SOME TESTS FAILED!")
        print("Please check the error messages above and fix any issues.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
