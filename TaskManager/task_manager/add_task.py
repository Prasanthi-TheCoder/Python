import json
from pathlib import Path
from .config import load_tasks,get_task_file



def save_tasks(tasks: list[dict], username: str) -> None:
    """
    Save tasks to file (e.g.<username>_tasks.json)
    :return: None
    """
    task_file = Path(get_task_file(username))
    with task_file.open("w") as file:
        json.dump(tasks, file, indent=4)



def add_task(username: str) -> None:
    """
    Add a new task to the tasks list
    :return: None
    """

    tasks = load_tasks(username)

    description: str = input("Enter task description: ")

    if tasks:
        task_id = tasks[-1]["id"] + 1
    else:
        task_id = 1

    task: dict = {
        "id": task_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks,username)

    print("\nTask added successfully!")
    print(f"Task ID   : {task_id}")
    print(f"Task      : {description}")
    print(f"Status    : Pending")


