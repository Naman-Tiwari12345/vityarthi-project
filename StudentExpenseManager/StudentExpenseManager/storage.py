import json
import os

DATA_FILE = os.path.join("data", "expenses.json")

def initialize_storage():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):
        default_data = {
            "users": {},
            "expenses": {},
            "budgets": {}
        }
        save_data(default_data)

def load_data():
    initialize_storage()

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
