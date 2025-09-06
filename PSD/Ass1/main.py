from database import ensure_bootstrap
first_time = ensure_bootstrap("seed_cars.csv", "car_rental.db")
print("Database ready (seeded from CSV)" if first_time else "Database ready (existing)")
# then start your CLI...
