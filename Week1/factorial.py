Numinput = input("Enter a number: ")
try:
    num = int(Numinput)
    factorial = 1
    i = 1

    if num < 0:
        print("Not defined for negative numbers.")
    elif num == 0:
        print("1.")
    else:
        while i <= num:
            factorial *= i
            i += 1
        print(f"The factorial of {num} is {factorial}.")

except ValueError:
    print("Please enter a valid integer.")

