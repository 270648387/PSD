import os
import database
from system import CarRentalSystem
from Utilities import (get_integer_input, get_float_input, get_yes_no_input)


def main():
    if not os.path.exists(database.DB_NAME):
        print("Database not found, initializing!")
        database.create_tables()
        database.import_cars_from_csv('seed_cars.csv')
        print("Car data successfully imported from CSV to database.")
        
    system = CarRentalSystem()
    current_user = None

    #Main page of the project
    while True:
        if not current_user:
            print("Welcome to Car Rental System!")
            print("1. Login")
            print("2. Register (Customers only)")
            print("3. Exit")
            choice = input("Please select an option: ")

            #User login and admin/customer getting different menu
            if choice == '1':
                username = input("Please enter username: ")
                password = input("Please enter password: ")
                user = system.authenticate_user(username, password)
                if user:
                    current_user = user
                    print("\nLogin successful!")

                    if current_user.get_role() == 'admin':
                        pending_count = len(system.get_rentals_by_status('pending'))
                        #Reminder for admin to manage pending bookings.
                        if pending_count > 0:
                            print(f"*Reminder*: You have {pending_count} pending rental requests.")
                    elif current_user.get_role() == 'customer':
                        rentals = system.get_customer_rentals(current_user.get_username())
                        approved_count = len([r for r in rentals if r.get_status() == 'approved'])
                        rejected_count = len([r for r in rentals if r.get_status() == 'rejected'])
                        #Reminders for customer about previous bookings.
                        if approved_count > 0:
                            print(f"*Reminder*: Your {approved_count} applications have been approved!")
                        if rejected_count > 0:
                            print(f"*Reminder*: Your {rejected_count} applications have been rejected!")

                else:
                    print("\nIncorrect username or password.")
                input("Press Enter to continue...")
            #User registration for customers.
            elif choice == '2':
                username = input("Please enter new username: ")
                password = input("Please enter new password: ")
                success, message = system.register_customer(username, password)
                print(f"\n{message}")
                input("Press Enter to continue...")
            #Exit the project.
            elif choice == '3':
                print("Thank you for using the car rental system, goodbye!")
                break
            else:
                print("Invalid input, please try again later.")
                input("Press Enter to continue...")
        
        #Successful log in and displaying different menu for admin and customer.
        else:
            print(f"Welcome, {current_user.get_username()})!")
            current_user.display_menu()

            choice = input("Please select an option: ")

            if current_user.get_role() == 'admin':
                handle_admin_actions(system, choice)
                if choice == '7': #Logout
                    current_user = None
            elif current_user.get_role() == 'customer':
                handle_customer_actions(system, current_user, choice)
                if choice == '5': #Logout
                    current_user = None


#Admin action options.
def handle_admin_actions(system, choice):
    if choice == '1':
        print("\n--- All Cars List ---")
        cars = system.get_all_cars()
        if not cars:
            print("No cars in the system.")
        else:
            for car in cars:
                print(car.get_details())
    elif choice == '2':
        print("\n--- Add New Car ---")
        car_id = input("Car ID (format: Car-XXX): ")
        if system.find_car_by_id(car_id):
            print("This car ID already exists, please re-enter.")
            input("Press Enter to return...")
            return

        make = input("Make: ")
        model = input("Model: ")
        year = get_integer_input("Year: ", 1980, 2025)
        mileage = get_integer_input("Mileage: ", 0)
        available_now = '1' if get_yes_no_input("Available now (y/n): ") else '0'
        min_rent_days = get_integer_input("Minimum rental days: ", 1)
        while True:
            max_rent_days = get_integer_input("Maximum rental days: ", min_rent_days)
            if max_rent_days >= min_rent_days:
                break
            else:
                print(f"Invalid input: Maximum rental days ({max_rent_days}) cannot be less than minimum rental days ({min_rent_days}).")
        daily_rate = get_float_input("Daily rate: ", 0.0)
        fuel_type = input("Fuel type (gasoline/hybrid/diesel): ")

        car_data = {
            'car_id': car_id,
            'make': make,
            'model': model,
            'year': year,
            'mileage': mileage,
            'available_now': available_now,
            'min_rent_days': min_rent_days,
            'max_rent_days': max_rent_days,
            'daily_rate': daily_rate,
            'fuel_type': fuel_type
        }
        success, message = system.add_car(car_data)
        print(f"\n{message}")
    elif choice == '3':
        print("\n--- Update Car Information ---")
        car_id = input("Please enter the car ID to update (e.g., Car-001): ")
        car = system.find_car_by_id(car_id)
        if car:
            print(f"Current information: {car.get_details()}")
            new_mileage_str = input(f"Please enter new mileage (current: {car.get_mileage()}, leave empty to keep current): ")
            new_mileage = int(new_mileage_str) if new_mileage_str.isdigit() else car.get_mileage()
            new_daily_rate_str = input(f"Please enter new daily rate (current: {car.get_daily_rate():.2f}, leave empty to keep current): ")
            new_daily_rate = float(new_daily_rate_str) if new_daily_rate_str else car.get_daily_rate()

            success, message = system.update_car(car_id, new_mileage, new_daily_rate)
            print(f"\n{message}")
        else:
            print("\nCar ID not found. Please ensure the format is correct (e.g., Car-001).")
    elif choice == '4':
        print("\n--- Delete Car ---")
        car_id = input("Please enter the car ID to delete: ")
        success, message = system.remove_car(car_id)
        print(f"\n{message}")
    elif choice == '5':
        print("\n--- All Rental Records ---")
        rentals = system.get_all_rentals()
        if not rentals:
            print("No rental records currently.")
        else:
            for rental in rentals:
                print(rental.get_details())
    elif choice == '6':
        print("\n--- Manage Rental Requests ---")
        pending_rentals = system.get_rentals_by_status('pending')
        if not pending_rentals:
            print("No pending rental requests currently.")
        else:
            print("--- Pending Rental Requests ---")
            for rental in pending_rentals:
                print(rental.get_details())

            rental_id = input("Please enter the rental ID to process (e.g., R-001): ")
            action = input("Please enter action (approve/reject): ")

            success, message = system.manage_rental_request(rental_id, action)
            print(f"\n{message}")
    elif choice == '7':
        print("\nLogging out...")
    else:
        print("\nInvalid choice, please try again.")
    input("\nPress Enter to return to menu...")


#Customer action options.
def handle_customer_actions(system, user, choice):
    if choice == '1':
        print("\n--- Available Cars List ---")
        cars = system.get_available_cars()
        if not cars:
            print("Sorry, no cars are currently available.")
        else:
            for car in cars:
                print(car.get_details())
    elif choice == '2':
        print("\n--- Rent a Car ---")
        car_id = input("Please enter the car ID you want to rent: ")
        car = system.find_car_by_id(car_id)
        if not car:
            print("\nInvalid car ID.")
            input("Press Enter to return...")
            return

        print(f"You selected {car.get_make()} {car.get_model()}, daily rate is ${car.get_daily_rate():.2f}.")
        days = get_integer_input("Please enter rental days: ")

        # Calculate total cost
        total_cost = days * car.get_daily_rate()
        print(f"Total rental cost is ${total_cost:.2f}.")

        if get_yes_no_input("Confirm booking? (y/n): "):
            rental, message = system.book_car(user.get_username(), car_id, days, 0.0)
            print(f"\n{message}")
        else:
            print("\nBooking cancelled.")

    elif choice == '3':
        print("\n--- My Rental Records ---")
        rentals = system.get_customer_rentals(user.get_username())
        if not rentals:
            print("You don't have any rental records yet.")
        else:
            for rental in rentals:
                print(rental.get_details())
    elif choice == '4':
        print("\n--- Return Car ---")
        rental_id = input("Please enter the rental ID to return (e.g., R-001): ")
        success, message, rental_cost = system.return_car(rental_id)
        print(f"\n{message}")
        if success:
            print(f"Total rental cost is ${rental_cost:.2f}.")
    elif choice == '5':
        print("\nLogging out...")
    else:
        print("\nInvalid choice, please try again.")
    input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()