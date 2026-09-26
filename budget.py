from storage import load_data, save_data
from validation import get_positive_amount

def set_budget(username):
    data = load_data()
    amount = get_positive_amount("Enter monthly budget: ")

    data["budgets"][username] = amount
    save_data(data)

    print(f"Monthly budget set to Rs.{amount:.2f}")

def check_budget(username):
    data = load_data()
    budget = data["budgets"].get(username, 0)
    expenses = data["expenses"].get(username, [])

    total = sum(item["amount"] for item in expenses)

    print(f"\nMonthly Budget : Rs.{budget:.2f}")
    print(f"Total Spending : Rs.{total:.2f}")

    if budget == 0:
        print("No budget has been set.")
    elif total > budget:
        print(f"Budget exceeded by Rs.{total - budget:.2f}")
    else:
        print(f"Remaining budget: Rs.{budget - total:.2f}")
