import database
from datetime import date, timedelta
from models import Admin, Customer, Car, Rental


class CarRentalSystem:
    _instance = None

    #CarRentalSystem implements the Singleton design pattern.
    #Only one central CarRentalSystem works for the whole project.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CarRentalSystem, cls).__new__(cls)
            cls._instance._users = []
            cls._instance._rentals = []
            cls._instance._initialize_system()
        return cls._instance

    def _initialize_system(self):
        #Load users from database
        user_rows = database.get_all_users_from_db()
        for row in user_rows:
            username, password, role = row
            if role == 'admin':
                self._users.append(Admin(username, password))
            elif role == 'customer':
                self._users.append(Customer(username, password))
        
        #Create default admin if no admin user exists
        if not any(user.get_role() == 'admin' for user in self._users):
            admin = Admin("admin", "password")
            self._users.append(admin)
            database.insert_user_into_db("admin", "password", "admin")
        
        #Load rental records from database
        rental_rows = database.get_all_rentals_from_db()
        max_rental_id = 0
        for row in rental_rows:
            rental_id, customer_username, car_id, start_date, end_date, total_cost, additional_fees, status, return_date = row
            rental = Rental(customer_username, car_id, start_date, end_date, total_cost, additional_fees, rental_id)
            rental._status = status
            rental._return_date = return_date
            self._rentals.append(rental)
            
            #Extract numeric part of rental ID to update _next_id
            if rental_id.startswith('R-'):
                try:
                    id_num = int(rental_id[2:])
                    max_rental_id = max(max_rental_id, id_num)
                except ValueError:
                    pass
        
        #Update Rental._next_id to avoid conflicts
        if max_rental_id > 0:
            Rental._next_id = max_rental_id + 1

    #Management of customer info
    def register_customer(self, username, password):
        if any(user.get_username() == username for user in self._users):
            return False, "Username already exists."
        new_customer = Customer(username, password)
        self._users.append(new_customer)
        database.insert_user_into_db(username, password, "customer")
        return True, "Customer registration successful."

    def authenticate_user(self, username, password):
        for user in self._users:
            if user.get_username() == username and user.check_password(password):
                return user
        return None
    
    #Admin management of cars
    def add_car(self, car_data):
        car_id = car_data['car_id']
        min_rent_days = car_data['min_rent_days']
        max_rent_days = car_data['max_rent_days']

        if min_rent_days > max_rent_days:
            return False, "Minimum rental days cannot be greater than maximum rental days."

        if database.get_car_by_id_from_db(car_id):
            return False, "Car ID already exists."

        database.insert_car_into_db(car_data)
        return True, "Car added successfully."

    def find_car_by_id(self, car_id):
        car_data = database.get_car_by_id_from_db(car_id)
        if car_data:
            return Car(
                car_id=car_data[0],
                make=car_data[1],
                model=car_data[2],
                year=car_data[3],
                mileage=car_data[4],
                available_now=car_data[5],
                min_rent_days=car_data[6],
                max_rent_days=car_data[7],
                daily_rate=car_data[8],
                fuel_type=car_data[9]
            )
        return None

    def update_car(self, car_id, new_mileage, new_daily_rate):
        car = self.find_car_by_id(car_id)
        if not car:
            return False, "Car ID not found."

        new_data = {
            'make': car.get_make(),
            'model': car.get_model(),
            'year': car.get_year(),
            'mileage': new_mileage,
            'available_now': car.is_available(),
            'min_rent_days': car.get_min_rent_days(),
            'max_rent_days': car.get_max_rent_days(),
            'daily_rate': new_daily_rate,
            'fuel_type': car.get_fuel_type()
        }
        database.update_car_in_db(car_id, new_data)
        return True, "Car information updated successfully."

    def remove_car(self, car_id):
        car = self.find_car_by_id(car_id)
        if not car:
            return False, "Car ID not found."
        if any(r.get_car_id() == car_id and r.get_status() in ['pending', 'approved'] for r in self._rentals):
            return False, "Cannot delete, this car has active rental records."
        database.delete_car_from_db(car_id)
        return True, "Car deleted successfully."

    def get_all_cars(self):
        car_rows = database.get_all_cars_from_db()
        return [Car(
            car_id=row[0], make=row[1], model=row[2], year=row[3],
            mileage=row[4], available_now=row[5], min_rent_days=row[6],
            max_rent_days=row[7], daily_rate=row[8], fuel_type=row[9]
        ) for row in car_rows]


    #Customer management of bookings
    def get_available_cars(self):
        all_cars = self.get_all_cars()
        return [car for car in all_cars if car.is_available()]

    def book_car(self, customer_username, car_id, rent_days, additional_fees):
        car = self.find_car_by_id(car_id)
        if not car:
            return None, "Invalid car ID."
        if not car.is_available():
            return None, "Sorry, this car is currently unavailable."
        if not (car.get_min_rent_days() <= rent_days <= car.get_max_rent_days()):
            return None, f"Rental days must be between {car.get_min_rent_days()} and {car.get_max_rent_days()} days."

        start_date = date.today()
        end_date = start_date + timedelta(days=rent_days)
        total_cost = rent_days * car.get_daily_rate() + additional_fees

        new_rental = Rental(customer_username, car_id, start_date, end_date, total_cost, additional_fees)
        self._rentals.append(new_rental)
        
        #Save rental to database
        rental_data = {
            'rental_id': new_rental.get_rental_id(),
            'customer_username': customer_username,
            'car_id': car_id,
            'start_date': str(start_date),
            'end_date': str(end_date),
            'total_cost': total_cost,
            'additional_fees': additional_fees,
            'status': 'pending',
            'return_date': None
        }
        database.insert_rental_into_db(rental_data)
        database.update_car_availability_in_db(car_id, False) 
        return new_rental, "Car booking successful! Your application has been submitted, please wait for admin approval."

    def return_car(self, rental_id):
        rental = self.find_rental_by_id(rental_id)
        if not rental:
            return False, "Rental ID not found.", 0
        if rental.get_status() != 'approved':
            return False, "This rental record is not in approved status, cannot return.", 0

        car = self.find_car_by_id(rental.get_car_id())
        if not car:
            return False, "Car associated with this rental record not found.", 0

        rental.return_car()
        database.update_rental_status_in_db(rental_id, 'returned', str(rental._return_date))
        database.update_car_availability_in_db(car.get_car_id(), True)  #After customer return the car it becomes available again
        return True, "Car returned successfully!", rental.get_total_cost()

    
    #Admin management of rental records
    def get_customer_rentals(self, username):
        return [r for r in self._rentals if r.get_customer() == username]

    def get_all_rentals(self):
        return self._rentals

    def get_rentals_by_status(self, status):
        return [r for r in self._rentals if r.get_status().lower() == status.lower()]

    def find_rental_by_id(self, rental_id):
        for rental in self._rentals:
            if rental.get_rental_id() == rental_id:
                return rental
        return None

    def manage_rental_request(self, rental_id, action):
        rental = self.find_rental_by_id(rental_id)
        if not rental:
            return False, "Rental ID not found."
        if rental.get_status() != 'pending':
            return False, "This rental request has already been processed, cannot repeat operation."

        car = self.find_car_by_id(rental.get_car_id())

        if action == 'approve':
            rental.approve()
            database.update_rental_status_in_db(rental_id, 'approved')
            return True, f"Rental {rental_id} has been approved."
        elif action == 'reject':
            rental.reject()
            database.update_rental_status_in_db(rental_id, 'rejected')
            if car:
                database.update_car_availability_in_db(car.get_car_id(), True)  #If a booking is rejected, the car becomes available again
            return True, f"Rental {rental_id} has been rejected."
        return False, "Invalid operation."