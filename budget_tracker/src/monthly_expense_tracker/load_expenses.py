import csv
from pathlib import Path
from typing import Any
from .save_expenses import save_expenses


def load_expenses() -> None:
    """
    Function to load expenses csv file and add expense records to the CSV file
    :return: None
    """
    expenses: list[Any] = []

    file_name: str = input("Enter file name: ")
    load_csv_file: Path = Path(file_name)

    with load_csv_file.open(mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Validate required fields
            if (row.get("date") and
                row.get("category") and
                row.get("amount") and
                row.get("description")):

                expense = {
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"]),
                    "description": row["description"]
                }
                expenses.append(expense)
            else:
                print("Skipping incomplete expense record.")
        save_expenses(expenses)