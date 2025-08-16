import math

def cartesian_to_polar(a, b):
    rho = math.sqrt(a**2 + b**2)          # Magnitude
    theta = math.atan2(b, a)              # Angle in radians
    return rho, theta

def polar_to_cartesian(rho, theta):
    a = rho * math.cos(theta)             # Real part
    b = rho * math.sin(theta)             # Imaginary part
    return a, b

print("Choose conversion type:")
print("1. Cartesian to Polar")
print("2. Polar to Cartesian")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    a = float(input("Enter real part: "))
    b = float(input("Enter imaginary part: "))
    rho, theta = cartesian_to_polar(a, b)
    print(f"Polar form: ρ = {rho:.4f}, θ = {theta:.4f} radians ({math.degrees(theta):.2f}°)")

elif choice == "2":
    rho = float(input("Enter magnitude ρ: "))
    theta = float(input("Enter angle θ in radians: "))
    a, b = polar_to_cartesian(rho, theta)
    print(f"Cartesian form: {a:.4f} + {b:.4f}i")

else:
    print("Invalid choice.")
