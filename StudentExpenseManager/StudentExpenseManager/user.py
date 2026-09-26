from storage import load_data, save_data
from validation import validate_username, validate_password

def register_user():
    data = load_data()

    username = input("Create username: ").strip()
    if not validate_username(username):
        print("Username must contain at least 3 characters.")
        return

    if username in data["users"]:
        print("Username already exists.")
        return

    password = input("Create password: ").strip()
    if not validate_password(password):
        print("Password must contain at least 4 characters.")
        return

    data["users"][username] = {"password": password}
    data["expenses"][username] = []
    data["budgets"][username] = 0
    save_data(data)

    print("Registration successful.")

def login_user():
    data = load_data()

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in data["users"] and data["users"][username]["password"] == password:
        print("Login successful. Welcome,", username)
        return username

    print("Invalid username or password.")
    return None
