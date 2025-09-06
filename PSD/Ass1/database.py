import sqlite3
import csv
import os


#Database system
#Created three tables, aiming to store necessary data such as user login and rental records etc.


DB_NAME = 'car_rental.db'


def connect_db():                                    #Connect to SQLite database
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():                                 #Creating all three tables
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            car_id TEXT PRIMARY KEY,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            available_now INTEGER NOT NULL,
            min_rent_days INTEGER NOT NULL,
            max_rent_days INTEGER NOT NULL,
            daily_rate REAL NOT NULL,
            fuel_type TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rentals (
            rental_id TEXT PRIMARY KEY,
            customer_username TEXT NOT NULL,
            car_id TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            total_cost REAL NOT NULL,
            additional_fees REAL NOT NULL,
            status TEXT NOT NULL,
            return_date TEXT,
            FOREIGN KEY (customer_username) REFERENCES users(username),
            FOREIGN KEY (car_id) REFERENCES vehicles(car_id)
        )
    ''')
    
    conn.commit()
    conn.close()

#Cars operations, importing car data from original csv file with all the colunms listed
def import_cars_from_csv(csv_filename):
    conn = connect_db()
    cur = conn.cursor()
    with open(csv_filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        to_insert = []
        for row in reader:
            to_insert.append((
                row['car_id'],
                row['make'],
                row['model'],
                int(row['year']),
                int(row['mileage']),
                int(row['available_now']),
                int(row['min_rent_days']),
                int(row['max_rent_days']),
                float(row['daily_rate']),
                row['fuel_type']
            ))

    cur.executemany('''
        INSERT INTO vehicles (car_id, make, model, year, mileage, available_now, 
                              min_rent_days, max_rent_days, daily_rate, fuel_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', to_insert)
    conn.commit()
    conn.close()


def get_all_cars_from_db():                      #return a list of all cars
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM vehicles')
    rows = cur.fetchall()
    conn.close()
    return rows


def get_car_by_id_from_db(car_id):               #return a single car accoring to its id
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM vehicles WHERE car_id = ?', (car_id,))
    row = cur.fetchone()
    conn.close()
    return row

##Adding, updating, or deleting car data 

def insert_car_into_db(car_data):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO vehicles (car_id, make, model, year, mileage, available_now, 
                              min_rent_days, max_rent_days, daily_rate, fuel_type)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (car_data['car_id'], car_data['make'], car_data['model'], car_data['year'],
          car_data['mileage'], car_data['available_now'], car_data['min_rent_days'],
          car_data['max_rent_days'], car_data['daily_rate'], car_data['fuel_type']))
    conn.commit()
    conn.close()


def update_car_in_db(car_id, new_data):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        UPDATE vehicles
        SET make = ?, model = ?, year = ?, mileage = ?, available_now = ?, 
            min_rent_days = ?, max_rent_days = ?, daily_rate = ?, fuel_type = ?
        WHERE car_id = ?
    ''', (new_data['make'], new_data['model'], new_data['year'], new_data['mileage'],
          new_data['available_now'], new_data['min_rent_days'], new_data['max_rent_days'],
          new_data['daily_rate'], new_data['fuel_type'], car_id))
    conn.commit()
    conn.close()


def delete_car_from_db(car_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM vehicles WHERE car_id = ?', (car_id,))
    conn.commit()
    conn.close()


def update_car_availability_in_db(car_id, availability_status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        UPDATE vehicles
        SET available_now = ?
        WHERE car_id = ?
    ''', (int(availability_status), car_id))
    conn.commit()
    conn.close()


def update_car_mileage_in_db(car_id, new_mileage):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        UPDATE vehicles
        SET mileage = ?
        WHERE car_id = ?
    ''', (new_mileage, car_id))
    conn.commit()
    conn.close()


# User database operations, for registration and login details
def insert_user_into_db(username, password, role):           #Creating new user login, storing in plain text to simplify the project.
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
    ''', (username, password, role))
    conn.commit()
    conn.close()


def get_user_from_db(username):                              #Fetching one user via username
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    row = cur.fetchone()
    conn.close()
    return row


def get_all_users_from_db():                                 #Fetching all users data
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    conn.close()
    return rows


# Rental database operations                                     
def insert_rental_into_db(rental_data):                      #Creating new rental records, such as R-001, test, Car-001 etc                      
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO rentals (rental_id, customer_username, car_id, start_date, end_date, 
                           total_cost, additional_fees, status, return_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (rental_data['rental_id'], rental_data['customer_username'], rental_data['car_id'],
          rental_data['start_date'], rental_data['end_date'], rental_data['total_cost'],
          rental_data['additional_fees'], rental_data['status'], rental_data['return_date']))
    conn.commit()
    conn.close()


def get_all_rentals_from_db():                               #Managing rental records in different ways
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM rentals')
    rows = cur.fetchall()
    conn.close()
    return rows


def get_rental_by_id_from_db(rental_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM rentals WHERE rental_id = ?', (rental_id,))
    row = cur.fetchone()
    conn.close()
    return row


def get_rentals_by_customer_from_db(customer_username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM rentals WHERE customer_username = ?', (customer_username,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_rentals_by_status_from_db(status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM rentals WHERE status = ?', (status,))
    rows = cur.fetchall()
    conn.close()
    return rows


def update_rental_status_in_db(rental_id, status, return_date=None):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        UPDATE rentals
        SET status = ?, return_date = ?
        WHERE rental_id = ?
    ''', (status, return_date, rental_id))
    conn.commit()
    conn.close()