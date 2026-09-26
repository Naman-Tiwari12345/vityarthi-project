from datetime import date
from storage import load_data, save_data
from validation import get_positive_amount

def add_expense(username):
    data = load_data()

    title = input("Expense name: ").strip()
    category = input("Category: ").strip().title()

    if not title or not category:
        print("Expense name and category cannot be empty.")
        return

    amount = get_positive_amount("Amount: ")
    expense = {
        "id": len(data["expenses"][username]) + 1,
        "title": title,
        "category": category,
        "amount": amount,
        "date": str(date.today())
    }

    data["expenses"][username].append(expense)
    save_data(data)
    print("Expense added successfully.")

def view_expenses(username):
    data = load_data()
    expenses = data["expenses"].get(username, [])

    if not expenses:
        print("No expenses recorded.")
        return

    print("\nID | Date | Category | Expense | Amount")
    print("-" * 55)

    for item in expenses:
        print(f'{item["id"]} | {item["date"]} | {item["category"]} | '
              f'{item["title"]} | Rs.{item["amount"]:.2f}')

def delete_expense(username):
    data = load_data()
    expenses = data["expenses"].get(username, [])

    if not expenses:
        print("No expenses available.")
        return

    view_expenses(username)

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for item in expenses:
        if item["id"] == expense_id:
            expenses.remove(item)
            save_data(data)
            print("Expense deleted successfully.")
            return

    print("Expense ID not found.")
