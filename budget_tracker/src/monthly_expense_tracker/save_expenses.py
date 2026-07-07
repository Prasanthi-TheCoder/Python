import csv
from .config import FILE_PATH, EXPENSE_FIELDS

def save_expenses(expenses) -> None:
    """
    Function to save expenses into csv file
    :param expenses:
            (dict[str, Any]): A dictionary containing the expense
            fields as string keys and their corresponding values.
            Example:
                {
                    "date": "2026-07-06",
                    "category": "Food",
                    "amount": 25.50,
                    "description": "Lunch"
                }
    :return: None
    """

    file_exists = FILE_PATH.exists()

    with FILE_PATH.open(mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=EXPENSE_FIELDS)

        if not file_exists:
            writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)

    print("Expense saved successfully!")