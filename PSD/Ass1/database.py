import sqlite3
import csv
from contextlib import closing
from pathlib import Path

DB_NAME = "car_rental.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    """Create cars table if it does not exist."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            car_id TEXT PRIMARY KEY,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER,
            available_now INTEGER CHECK (available_now IN (0,1)),
            min_rent_days INTEGER,
            max_rent_days INTEGER,
            daily_rate REAL,
            fuel_type TEXT
        )
        """)
        conn.commit()


# Rental car management

def add_car(car_id, make, model, year, mileage, available_now,
            min_rent_days, max_rent_days, daily_rate, fuel_type):
    """Insert a new car into the database."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("""
            INSERT INTO cars
            (car_id, make, model, year, mileage, available_now,
             min_rent_days, max_rent_days, daily_rate, fuel_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (car_id, make, model, year, mileage, available_now,
              min_rent_days, max_rent_days, daily_rate, fuel_type))
        conn.commit()

def list_cars(only_available=False):
    with get_connection() as conn, closing(conn.cursor()) as cur:
        if only_available:
            cur.execute("SELECT * FROM cars WHERE available_now=1 ORDER BY car_id")
        else:
            cur.execute("SELECT * FROM cars ORDER BY car_id")
        return cur.fetchall()


def find_car(car_id):
    """Fetch a single car by ID."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("SELECT * FROM cars WHERE car_id=?", (car_id,))
        return cur.fetchone()

def update_mileage(car_id, new_mileage):
    """Update mileage for a specific car."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("UPDATE cars SET mileage=? WHERE car_id=?", (new_mileage, car_id))
        conn.commit()

def update_rate(car_id, new_rate):
    """Update daily rate for a specific car."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("UPDATE cars SET daily_rate=? WHERE car_id=?", (new_rate, car_id))
        conn.commit()

def set_availability(car_id, available: bool):
    """Set availability of a car (True/False)."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("UPDATE cars SET available_now=? WHERE car_id=?", (1 if available else 0, car_id))
        conn.commit()

def delete_car(car_id):
    """Delete a car from the database."""
    with get_connection() as conn, closing(conn.cursor()) as cur:
        cur.execute("DELETE FROM cars WHERE car_id=?", (car_id,))
        conn.commit()


# CSV Import

def import_from_csv(csv_file, overwrite=False):
    """
    Import cars from a CSV file.
    """
    csv_path = Path(csv_file)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_file}")

    with get_connection() as conn, closing(conn.cursor()) as cur, open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        if overwrite:
            cur.execute("DELETE FROM cars")

        for row in reader:
            cur.execute("""
                INSERT OR REPLACE INTO cars
                (car_id, make, model, year, mileage, available_now,
                 min_rent_days, max_rent_days, daily_rate, fuel_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["car_id"], row["make"], row["model"],
                int(row["year"]), int(row["mileage"]),
                int(row["available_now"]),
                int(row["min_rent_days"]), int(row["max_rent_days"]),
                float(row["daily_rate"]), row["fuel_type"]
            ))
        conn.commit()
