### Showcasing the use of all OO concepts such as encapsulation, abstraction, inheritance and polymorphism


import abc
from datetime import date

#Abstraction base class
class User(abc.ABC):

    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role

    #Encapsulation, adding getter methods, protected access
    def get_username(self):
        return self._username 
    
    def get_role(self):
        return self._role

    def check_password(self, password):
        return self._password == password

    @abc.abstractmethod
    def display_menu(self):
        pass


#Inheritance: Admin and Customer inherit from User ---
class Admin(User):

    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def display_menu(self):
        print("\n--- Admin Menu ---")
        print("1. View all cars")
        print("2. Add car")
        print("3. Update car information")
        print("4. Delete car")
        print("5. View all rental records")
        print("6. Approve/Reject rental requests")
        print("7. Logout")
        print("--------------------")


class Customer(User):

    def __init__(self, username, password):
        super().__init__(username, password, "customer")
    
    #Polymorphism, calling same method on different objects and show different behavior
    def display_menu(self):
        print("\n--- Customer Menu ---")
        print("1. View all available cars")
        print("2. Rent a car")
        print("3. View my rental records")
        print("4. Return car")
        print("5. Logout")
        print("------------------")


class Car:
    
    #Encapsulation with protected attributes, getter and setter methods.
    def __init__(self, car_id, make, model, year, mileage, available_now, min_rent_days, max_rent_days, daily_rate,
                 fuel_type):
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
    
    def get_fuel_type(self):
        return self._fuel_type

    #Updating attributes
    def update_details(self, make, model, year, mileage, daily_rate, availability):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._daily_rate = daily_rate
        self._available_now = availability

    #Mileage can not be rolled back
    def update_mileage(self, new_mileage: int):
        if new_mileage > self._mileage:
            self._mileage = new_mileage

    def get_details(self):
        availability = "Yes" if self._available_now else "No"
        return (f"ID: {self._car_id}, Make: {self._make}, Model: {self._model}, Year: {self._year}, "
                f"Mileage: {self._mileage} km, Daily Rate: ${self._daily_rate:.2f}, Currently Available: {availability}")


#Encapsulation to manage rental booking details
class Rental:
    _next_id = 1

    def __init__(self, customer_username, car_id, start_date, end_date, total_cost, additional_fees, rental_id=None):
        if rental_id:
            self._rental_id = rental_id
        else:
            self._rental_id = f"R-{Rental._next_id:03d}"
            Rental._next_id += 1
        self._customer_username = customer_username
        self._car_id = car_id
        self._start_date = start_date
        self._end_date = end_date
        self._total_cost = total_cost
        self._additional_fees = additional_fees
        self._status = "pending"               
        self._return_date = None
    #Generate rental id automatically like R-001
    
    
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

    # Status can be: pending, approved, rejected, returned
    def get_status(self):
        return self._status
    
    #Example :Rental id :R-001, Customer: test, Car id: Car-001 etc
    def get_details(self):
        return_info = f", Return Date: {self._return_date}" if self._return_date else ""
        return (f"Rental ID: {self._rental_id}, Customer: {self._customer_username}, "
                f"Car ID: {self._car_id}, Rental Period: {self._start_date} to {self._end_date}, "
                f"Total Cost: ${self._total_cost:.2f}, Status: {self._status}{return_info}")