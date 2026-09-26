from collections import defaultdict
from storage import load_data

def generate_report(username):
    data = load_data()
    expenses = data["expenses"].get(username, [])

    if not expenses:
        print("No expenses available for report.")
        return

    total = sum(item["amount"] for item in expenses)
    categories = defaultdict(float)

    for item in expenses:
        categories[item["category"]] += item["amount"]

    highest_category = max(categories, key=categories.get)

    print("\n========== EXPENSE REPORT ==========")
    print(f"Total Expenses: Rs.{total:.2f}")
    print(f"Number of Transactions: {len(expenses)}")
    print(f"Highest Spending Category: {highest_category}")
    print(f"Amount Spent in Category: Rs.{categories[highest_category]:.2f}")

    print("\nCategory-wise Spending:")
    for category, amount in categories.items():
        percentage = (amount / total) * 100
        print(f"{category}: Rs.{amount:.2f} ({percentage:.1f}%)")
