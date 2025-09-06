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
    