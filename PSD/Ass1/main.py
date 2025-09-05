from database import init_db, import_from_csv, list_cars

init_db()

# Import from CSV
import_from_csv("seed_cars.csv", overwrite=True)

# Show all cars
cars = list_cars()
for car in cars:
    print(car)
