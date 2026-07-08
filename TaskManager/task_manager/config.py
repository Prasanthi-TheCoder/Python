from pathlib import Path
import json


#common variables
FILE_PATH = Path("users.json")
TASK_FILE = Path("tasks.json")



#common functions
def get_task_file(username: str) -> Path:
    """
    Return task file based on username
    """
    return Path(f"{username}_tasks.json")


def load_tasks(username: str) -> list:
    """
    Load user's tasks from file
    :return: list of tasks
    """
    task_file = get_task_file(username)
    if not task_file.exists():
        return []
    try:
        with task_file.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []