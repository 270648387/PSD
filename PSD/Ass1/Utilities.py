#Force user to enter a valid input
def get_validated_input(prompt, validation_func, error_message):

    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(f"Invalid input: {error_message}")

#Get integer input within the min and max value
def get_integer_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Error: Input value cannot be less than {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Error: Input value cannot be greater than {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input: Please enter a valid integer.")

#Get float input within the min and max value
def get_float_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                 print(f"Error: Input value cannot be less than {min_val}.")
                 continue
            if max_val is not None and value > max_val:
                print(f"Error: Input value cannot be greater than {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input: Please enter a valid number.")

#Get y, n, yes, no input.
def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid input: Please enter 'y' or 'n'.")