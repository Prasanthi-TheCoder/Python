import csv
from .config import FILE_PATH

def enter_monthly_budget() -> float:
    """
    Function to enter monthly budget
    :return: float: monthly budget
    """
    budget: float = 0
    while True:
        try:
            budget = float(input("Enter your monthly budget amount: "))
            if budget < 0:
                print("Budget cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
    return budget


def calculate_total_expenses() -> None:
    """
    Function to calculate total expenses based on monthly budget
    :return: None
    """
    total_expenses = 0
    budget: float = enter_monthly_budget()

    if FILE_PATH.exists():
        with FILE_PATH.open("r", newline="") as file:
            reader = csv.DictReader(file)
            for expense in reader:
                if expense.get("amount"):
                    total_expenses += float(expense["amount"])
    else:
        print("No expense file found.")
    print("\n========== Budget Status ==========")

    print(f"Monthly Budget : ${budget:.2f}")
    print(f"Total Expenses : ${total_expenses:.2f}")

    if total_expenses > budget:
        print("You have exceeded your budget!")
        print(f"Exceeded Amount: ${total_expenses - budget:.2f}")
    else:
        remaining = budget - total_expenses
        print(f"You have ${remaining:.2f} left for the month.")

    print("===================================")