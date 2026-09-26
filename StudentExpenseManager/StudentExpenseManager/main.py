from user import register_user, login_user
from expenses import add_expense, view_expenses, delete_expense
from budget import set_budget, check_budget
from reports import generate_report
from storage import initialize_storage

def expense_menu(username):
    while True:
        print("\n===== EXPENSE MANAGER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Set Monthly Budget")
        print("5. Check Budget")
        print("6. Generate Report")
        print("7. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense(username)
        elif choice == "2":
            view_expenses(username)
        elif choice == "3":
            delete_expense(username)
        elif choice == "4":
            set_budget(username)
        elif choice == "5":
            check_budget(username)
        elif choice == "6":
            generate_report(username)
        elif choice == "7":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    initialize_storage()

    while True:
        print("\n===== STUDENT EXPENSE & BUDGET MANAGEMENT SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                expense_menu(username)
        elif choice == "3":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
