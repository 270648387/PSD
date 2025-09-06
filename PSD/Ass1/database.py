import sqlite3
import csv, os
from datetime import date
from typing import List, Optional, Tuple, Dict, Any
from contextlib import closing
from pathlib import Path

#Manage database using SQLite
class DbManager:
    def __init__(self, db_path: str = "car_rental.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self) -> sqlite3.Connection:   #get database connection
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  
        return conn
    
    def init_database(self):                          #initialise setup database
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create the users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL CHECK (role IN ('admin', 'customer'))
                )
            ''')

            # Create the cars table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cars (
                    car_id TEXT PRIMARY KEY,
                    make TEXT NOT NULL,
                    model TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    mileage INTEGER NOT NULL,
                    available_now BOOLEAN NOT NULL,
                    min_rent_days INTEGER NOT NULL,
                    max_rent_days INTEGER NOT NULL,
                    daily_rate REAL NOT NULL,
                    fuel_type TEXT NOT NULL
                )
            ''')
            
            # Create the rentals table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rentals (
                    rental_id TEXT PRIMARY KEY,
                    customer_username TEXT NOT NULL,
                    car_id TEXT NOT NULL,
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL,
                    total_cost REAL NOT NULL,
                    additional_fees REAL NOT NULL,
                    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'returned')),
                    return_date DATE,
                    FOREIGN KEY (customer_username) REFERENCES users(username),
                    FOREIGN KEY (car_id) REFERENCES cars(car_id)
                )
            ''')
            
            # Create the rental IDs table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sequences (
                    name TEXT PRIMARY KEY,
                    value INTEGER NOT NULL
                )
            ''')
            cursor.execute('''
                INSERT OR IGNORE INTO sequences (name, value) 
                VALUES ('rental_id', 0)
            ''')

            # Set up default admin account
            cursor.execute('''
                INSERT OR IGNORE INTO users (username, password, role) 
                VALUES ('admin', 'password', 'admin')
            ''')
            
            conn.commit()
    



    # User operations
    def add_user(self, username: str, password: str, role: str) -> bool:
        """Add a new user"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                    (username, password, role)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        """Get user by username"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate user"""
        user = self.get_user(username)
        if user and user['password'] == password:
            return user
        return None
    
    # Car operations
    def add_car(self, car_data: Dict[str, Any]) -> bool:
        """Add a new car"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO cars (car_id, make, model, year, mileage, available_now, 
                                    min_rent_days, max_rent_days, daily_rate, fuel_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    car_data['car_id'], car_data['make'], car_data['model'], 
                    car_data['year'], car_data['mileage'], car_data['available_now'],
                    car_data['min_rent_days'], car_data['max_rent_days'], 
                    car_data['daily_rate'], car_data['fuel_type']
                ))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def get_car(self, car_id: str) -> Optional[Dict[str, Any]]:
        """Get car by ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cars WHERE car_id = ?', (car_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_all_cars(self) -> List[Dict[str, Any]]:
        """Get all cars"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cars')
            return [dict(row) for row in cursor.fetchall()]
    
    def get_available_cars(self) -> List[Dict[str, Any]]:
        """Get available cars"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cars WHERE available_now = 1')
            return [dict(row) for row in cursor.fetchall()]
    
    def update_car(self, car_id: str, **kwargs) -> bool:
        """Update car information"""
        if not kwargs:
            return False
        
        set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values()) + [car_id]
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'UPDATE cars SET {set_clause} WHERE car_id = ?', values)
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_car(self, car_id: str) -> bool:
        """Delete car"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM cars WHERE car_id = ?', (car_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    # Rental operations
    def get_next_rental_id(self) -> str:
        """Get next rental ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE sequences SET value = value + 1 WHERE name = "rental_id"')
            cursor.execute('SELECT value FROM sequences WHERE name = "rental_id"')
            next_id = cursor.fetchone()[0]
            conn.commit()
            return f"R-{next_id:03d}"
    
    def add_rental(self, rental_data: Dict[str, Any]) -> bool:
        """Add a new rental"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO rentals (rental_id, customer_username, car_id, start_date, 
                                       end_date, total_cost, additional_fees, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    rental_data['rental_id'], rental_data['customer_username'], 
                    rental_data['car_id'], rental_data['start_date'], 
                    rental_data['end_date'], rental_data['total_cost'], 
                    rental_data['additional_fees'], rental_data['status']
                ))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
    
    def get_rental(self, rental_id: str) -> Optional[Dict[str, Any]]:
        """Get rental by ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rentals WHERE rental_id = ?', (rental_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_all_rentals(self) -> List[Dict[str, Any]]:
        """Get all rentals"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rentals')
            return [dict(row) for row in cursor.fetchall()]
    
    def get_customer_rentals(self, username: str) -> List[Dict[str, Any]]:
        """Get rentals for a specific customer"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rentals WHERE customer_username = ?', (username,))
            return [dict(row) for row in cursor.fetchall()]
    
    def get_rentals_by_status(self, status: str) -> List[Dict[str, Any]]:
        """Get rentals by status"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rentals WHERE status = ?', (status,))
            return [dict(row) for row in cursor.fetchall()]
    
    def update_rental(self, rental_id: str, **kwargs) -> bool:
        """Update rental information"""
        if not kwargs:
            return False
        
        set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values()) + [rental_id]
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'UPDATE rentals SET {set_clause} WHERE rental_id = ?', values)
            conn.commit()
            return cursor.rowcount > 0
    
    def has_active_rental(self, car_id: str) -> bool:
        """Check if car has active rental"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT COUNT(*) FROM rentals 
                WHERE car_id = ? AND status IN ('pending', 'approved')
            ''', (car_id,))
            return cursor.fetchone()[0] > 0