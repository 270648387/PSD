# Library Management System - Python Implementation

A comprehensive Python-based Library Management System that manages books, library members, borrowing processes, and fine calculations. This system demonstrates object-oriented programming principles and provides both programmatic and interactive interfaces.

## 🚀 Features

### Core Functionality
- **Book Management**: Add, remove, update, and search books with genre categorization
- **Member Management**: Register members, track membership status, and manage contact information
- **Borrowing System**: Complete borrowing workflow with validation and limits
- **Return Processing**: Automated fine calculation and inventory updates
- **Fine Management**: Overdue penalty calculation and payment tracking
- **Reporting**: Comprehensive library statistics and member history

### Business Rules Implemented
- ✅ Maximum 5 books per member
- ✅ 14-day loan period
- ✅ $1.00 per day overdue fine
- ✅ Membership expiration validation
- ✅ Real-time inventory tracking
- ✅ Automatic fine generation

## 📁 Project Structure

```
Library_Management_System/
├── models.py              # Core data models (Book, Member, BorrowRecord, Fine)
├── library_system.py      # Main system controller and business logic
├── demo.py               # Comprehensive demonstration script
├── cli.py                # Interactive command-line interface
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external packages required (uses only standard library)

### Quick Start
1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd Library_Management_System
   ```
3. **Run the demo** to see the system in action:
   ```bash
   python demo.py
   ```
4. **Or start the interactive CLI**:
   ```bash
   python cli.py
   ```

## 🎯 Usage Examples

### Programmatic Usage

```python
from models import Book, Member, Genre
from library_system import LibrarySystem
from datetime import datetime, timedelta

# Initialize the system
library = LibrarySystem()

# Add a book
book = Book("Python Programming", "John Doe", "978-1234567890", 
            datetime.now(), Genre.TECHNOLOGY, 3)
library.add_book(book)

# Add a member
member = Member("Alice Smith", "alice@email.com", "555-0101", 
               "123 Main St", datetime.now() + timedelta(days=365))
library.add_member(member)

# Borrow a book
borrow_record = library.borrow_book(book.get_book_id(), member.get_member_id())

# Generate a report
report = library.generate_report()
print(report)
```

### Interactive CLI

The command-line interface provides a user-friendly way to interact with the system:

```bash
python cli.py
```

**Main Menu Options:**
1. **Book Management** - Add, remove, update, and search books
2. **Member Management** - Register and manage library members
3. **Borrowing Operations** - Borrow books and manage loans
4. **Return Operations** - Return books and process fines
5. **Fine Management** - View and process overdue fines
6. **Search & Reports** - Generate reports and search functionality
7. **Run Demo** - Execute the comprehensive demonstration

## 🔧 System Architecture

### Class Design
- **`Book`**: Manages book information, availability, and copy tracking
- **`Member`**: Handles member data, borrowing limits, and membership validation
- **`BorrowRecord`**: Tracks individual borrowing transactions and due dates
- **`Fine`**: Manages overdue penalties and payment processing
- **`LibrarySystem`**: Coordinates all operations and maintains system state
- **`Genre`**: Enumeration of book categories

### Key Relationships
- One member can have multiple borrow records
- One book can be involved in multiple borrow records
- One borrow record can generate one fine
- LibrarySystem manages all collections and operations

## 📊 Demo Script

The `demo.py` script demonstrates all system functionality:

- **Book Management**: Adding, searching, and updating books
- **Member Management**: Registration and status checking
- **Borrowing Process**: Complete workflow with validation
- **Return Process**: Fine calculation and inventory updates
- **Error Handling**: Graceful handling of edge cases
- **Reporting**: Comprehensive system statistics

Run with: `python demo.py`

## 🧪 Testing

The system includes comprehensive error handling and validation:

- **Input Validation**: All user inputs are validated
- **Business Rule Enforcement**: Borrowing limits and membership validation
- **Error Recovery**: Graceful handling of invalid operations
- **State Consistency**: Automatic updates maintain data integrity

## 🚀 Future Enhancements

### Planned Features
- **Database Integration**: Persistent storage with SQLite/PostgreSQL
- **Web Interface**: Flask/Django web application
- **Email Notifications**: Automated reminders for due dates
- **Reservation System**: Book reservation functionality
- **Advanced Analytics**: Usage patterns and library statistics
- **Mobile API**: RESTful API for mobile applications

### Extensibility
The system is designed to be easily extensible:
- New genres can be added to the Genre enum
- Fine calculation rates are configurable
- Report generation supports custom queries
- Business rules can be modified in the LibrarySystem class

## 📝 API Reference

### Core Methods

#### LibrarySystem
- `add_book(book)` - Add a new book
- `borrow_book(book_id, member_id)` - Borrow a book
- `return_book(borrow_id)` - Return a borrowed book
- `search_book(query)` - Search books by title/author/ISBN
- `generate_report()` - Generate comprehensive report

#### Book
- `is_available()` - Check if book can be borrowed
- `decrease_available_copies()` - Reduce available copies
- `increase_available_copies()` - Increase available copies

#### Member
- `can_borrow_book()` - Check borrowing eligibility
- `borrow_book()` - Increment borrowed book count
- `return_book()` - Decrement borrowed book count

## 🤝 Contributing

This system is designed as a learning tool and demonstration of Python OOP principles. Feel free to:

- **Extend functionality** with new features
- **Improve error handling** and validation
- **Add unit tests** for better code coverage
- **Optimize performance** for larger datasets
- **Create additional interfaces** (web, mobile, etc.)

## 📄 License

This project is provided as educational software. Feel free to use, modify, and distribute as needed.

## 🎓 Learning Objectives

This implementation demonstrates:
- **Object-Oriented Programming** principles and design patterns
- **Data modeling** and relationship management
- **Business logic implementation** and validation
- **User interface design** (CLI and programmatic)
- **Error handling** and system robustness
- **Code organization** and modularity

---

🏛️ **The Library Management System provides a solid foundation for learning Python OOP and building production-ready library software!** 📚
