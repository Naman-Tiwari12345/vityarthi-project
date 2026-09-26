def validate_username(username):
    return len(username) >= 3

def validate_password(password):
    return len(password) >= 4

def get_positive_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount > 0:
                return amount
            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")
