from .add_task import save_tasks
from .config import load_tasks



def delete_task(username: str) -> None:
    """
    Delete a task
    :param username:
    :return: None
    """
    tasks = load_tasks(username)
    task_id_to_delete = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id_to_delete:
            tasks.remove(task)

    save_tasks( tasks, username )