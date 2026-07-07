from pathlib import Path
from typing import Any

# Common variables
FILE_PATH = Path("expenses.csv")
DATE_FORMAT: str = "%Y-%m-%d"
EXPENSE_FIELDS: list[str] = [
    "date",
    "category",
    "amount",
    "description"
]

EXPENSES_CSV: list[Any] = []
