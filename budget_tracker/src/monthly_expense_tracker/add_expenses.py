from datetime import datetime
from .config import EXPENSES_CSV,DATE_FORMAT
from .save_expenses import save_expenses

def validate_date(date_string) -> bool:
    """
    Function to validate date format
    :param date_string: date string
    :return: True or False
    """
    try:
        datetime.strptime(date_string, DATE_FORMAT)
        return True
    except ValueError:
        return False


def add_expenses() -> None:
    """
    Function to add expenses
    :return: None
    """
    # Validate date
    while True:
        while True:
            date = input("Enter expense date (YYYY-MM-DD): ")

            if validate_date(date):
                break
            else:
                print("Error: Invalid date. Please enter date in YYYY-MM-DD format.")

        category = input("Enter category (Food, Travel, etc.): ")

        # Validate amount
        while True:
            try:
                amount = float(input("Enter amount spent: "))

                if amount < 0:
                    print("Error: Amount cannot be negative.")
                    continue
                break

            except ValueError:
                print("Error: Please enter a valid amount.")

        description = input("Enter expense description: ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        EXPENSES_CSV.append(expense)
        print("\nExpense added successfully!")
        choice = input("Do you want to add another expense? (y/n): ").lower()

        if choice != "y":
            save_expenses(EXPENSES_CSV)
            break
