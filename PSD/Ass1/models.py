import abc
from datetime import date
from database import DbManager

class User(abc.ABC):
    #  Use of abstraction
    def __init__(self, username, password, role):
        self._username = username
        self._password = password   
        self._role = role 

    #  Use of encapsulation, add getter methods
    def get_username(self):
        return self._username 
    
    def get_role(self):
        return self._role 
    
    def check_password(self, password):
        return self._password == password 
    

    @abc.abstractmethod
    def display_menu(self):
        pass


# --- Inheritance: Admin and Customer inherit from User ---
class Admin(User):

    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def display_menu(self):
        """Admin operation menu."""
        print("\n--- Admin Menu ---")
        print("1. View All Cars")
        print("2. Add Car")
        print("3. Update Car Information")
        print("4. Delete Car")
        print("5. View All Rental Records")
        print("6. Filter Rental Records by Status (pending, approved, rejected)")
        print("7. Approve/Reject Rental Applications")
        print("8. Logout")
        print("--------------------")


class Customer(User):

    def __init__(self, username, password):
        super().__init__(username, password, "customer")

    def display_menu(self):
        """Customer operation menu."""
        print("\n--- Customer Menu ---")
        print("1. View All Available Cars")
        print("2. Rent a Car")
        print("3. View My Rental Records")
        print("4. Return Car")
        print("5. Logout")
        print("------------------")


class Car:
    _db = DbManager()

    def __init__(self, car_id, make, model, year, mileage, available_now, min_rent_days, max_rent_days, daily_rate,
                 fuel_type):
        # Encapsulate all car attributes
        self._car_id = car_id
        self._make = make
        self._model = model
        self._year = int(year)
        self._mileage = int(mileage)
        self._available_now = bool(int(available_now))
        self._min_rent_days = int(min_rent_days)
        self._max_rent_days = int(max_rent_days)
        self._daily_rate = float(daily_rate)
        self._fuel_type = fuel_type

    @classmethod
    def from_dict(cls, data):
        """Create Car instance from database dictionary"""
        return cls(
            car_id=data['car_id'],
            make=data['make'],
            model=data['model'],
            year=data['year'],
            mileage=data['mileage'],
            available_now=data['available_now'],
            min_rent_days=data['min_rent_days'],
            max_rent_days=data['max_rent_days'],
            daily_rate=data['daily_rate'],
            fuel_type=data['fuel_type']
        )

    # --- Encapsulation: Provide a series of getter and setter methods to control access to attributes ---
    def get_car_id(self):
        return self._car_id

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_mileage(self):
        return self._mileage

    def get_daily_rate(self):
        return self._daily_rate

    def is_available(self):
        return self._available_now

    def set_availability(self, status: bool):
        self._available_now = status

    def get_min_rent_days(self):
        return self._min_rent_days

    def get_max_rent_days(self):
        return self._max_rent_days

    def update_details(self, make, model, year, mileage, daily_rate, availability):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._daily_rate = daily_rate
        self._available_now = availability

    def update_mileage(self, new_mileage: int):
        if new_mileage > self._mileage:
            self._mileage = new_mileage

    def get_details(self):
        availability = "Yes" if self._available_now else "No"
        return (f"ID: {self._car_id}, Make: {self._make}, Model: {self._model}, Year: {self._year}, "
                f"Mileage: {self._mileage} km, Daily Rate: ${self._daily_rate:.2f}, Currently Available: {availability}")


class Rental:
    _db = DbManager()

    def __init__(self, customer_username, car_id, start_date, end_date, total_cost, additional_fees, rental_id=None):
        if rental_id:
            self._rental_id = rental_id
        else:
            self._rental_id = self._db.get_next_rental_id()
        self._customer_username = customer_username
        self._car_id = car_id
        self._start_date = start_date
        self._end_date = end_date
        self._total_cost = total_cost
        self._additional_fees = additional_fees
        self._status = "pending"  # Status can be: pending, approved, rejected, returned
        self._return_date = None

    @classmethod
    def from_dict(cls, data):
        """Create Rental instance from database dictionary"""
        rental = cls(
            customer_username=data['customer_username'],
            car_id=data['car_id'],
            start_date=date.fromisoformat(data['start_date']),
            end_date=date.fromisoformat(data['end_date']),
            total_cost=data['total_cost'],
            additional_fees=data['additional_fees'],
            rental_id=data['rental_id']
        )
        rental._status = data['status']
        rental._return_date = date.fromisoformat(data['return_date']) if data.get('return_date') else None
        return rental

    def get_rental_id(self):
        return self._rental_id

    def get_car_id(self):
        return self._car_id

    def get_customer(self):
        return self._customer_username

    def get_total_cost(self):
        return self._total_cost

    def approve(self):
        self._status = "approved"

    def reject(self):
        self._status = "rejected"

    def return_car(self):
        self._status = "returned"
        self._return_date = date.today()

    def get_status(self):
        return self._status

    def get_details(self):
        return_info = f", Return Date: {self._return_date}" if self._return_date else ""
        return (f"Rental ID: {self._rental_id}, Customer: {self._customer_username}, "
                f"Car ID: {self._car_id}, Rental Period: {self._start_date} to {self._end_date}, "
                f"Total Cost: ${self._total_cost:.2f} (Additional Fees: ${self._additional_fees:.2f}), Status: {self._status}{return_info}")


    


    