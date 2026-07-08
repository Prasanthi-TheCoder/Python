from .config import load_tasks



def view_tasks(username: str) -> None:
    """
    Display all tasks for logged-in user
    :param username:
    :return: None
    """

    tasks = load_tasks(username)

    if not tasks:
        print("\nNo tasks found!")
        return

    print(f"\n===== {username}'s Tasks =====")

    for task in tasks:
        print("-------------------------")
        print(f"Task ID    : {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status     : {task['status']}")

    print("-------------------------")


