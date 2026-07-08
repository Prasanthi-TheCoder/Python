from .add_task import save_tasks
from .config import load_tasks



def mark_task_status(username: str) -> None:
    """
    Mark a task as completed
    :param username:
    :return: None
    """
    tasks = load_tasks(username)

    if  not tasks:
        return
    try:
        for task in tasks:
            task["status"] = "Completed"
    except KeyError as ke:
        print(f"KeyError: {ke}")

    save_tasks(tasks, username)

