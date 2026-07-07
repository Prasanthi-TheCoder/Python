import csv
from tabulate import tabulate
from .config import FILE_PATH

def view_expenses() -> None:
    """
    Function to display the expense details from CSV file
    :return: None
    """
    expenses = []

    if not FILE_PATH.exists():
        print("No expense file found.")
        return

    with FILE_PATH.open("r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if all([
                row.get("date"),
                row.get("category"),
                row.get("amount"),
                row.get("description")
            ]):
                expenses.append([
                    row["date"],
                    row["category"],
                    float(row["amount"]),
                    row["description"]
                ])

    if not expenses:
        print("No expenses found.")
        return

    print("\nExpense Details\n")

    print(tabulate(
        expenses,
        headers=[
            "Date",
            "Category",
            "Amount",
            "Description"
        ],
        tablefmt="grid"
    ))