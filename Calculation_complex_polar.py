import math

def to_rad(theta):
    return math.radians(theta) 

def to_deg(theta):
    return math.degrees(theta) 

def multiply_polar(r1, th1, r2, th2):
    th1, th2 = to_rad(th1), to_rad(th2)
    r = r1 * r2
    theta = th1 + th2
    return r, to_deg(theta) 

def divide_polar(r1, th1, r2, th2):
    if r2 == 0:
        raise ZeroDivisionError("Cannot divide by zero magnitude complex number.")
    th1, th2 = to_rad(th1), to_rad(th2)
    r = r1 / r2
    theta = th1 - th2
    return r, to_deg(theta) 

print(f"\nPlease enter the first Polar coordinate:\n")
r1 = float(input("Magnitude:"))
th1 = float(input("Angle:"))

print(f"\nPlease enter the second Polar coordinate:\n")
r2 = float(input("Magnitude:"))
th2 = float(input("Angle:"))

prod = multiply_polar(r1,th1,r2,th2)
quot = divide_polar(r1,th1,r2,th2)

print(f"\nc1 * c2 : ({prod[0]:.2f}, {prod[1]:.2f}°)")
print(f"\nc1 / c2 : ({quot[0]:.2f}, {quot[1]:.2f}°)")
