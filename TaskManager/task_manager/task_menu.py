from .add_task import add_task
from .view_task import view_tasks
from .mark_task import mark_task_status
from .delete_task import delete_task



def menu(username: str) -> None:
    """
    Function that displays the tasks menu
    :param username:
    :return: None
    """
    while True:
        print("\n====== TASK MANAGER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Logout")

        choice = input("Enter your choice: ")
        uname = username.upper()

        if choice == "1":
            add_task(uname)
        elif choice == "2":
            view_tasks(uname)
        elif choice == "3":
            mark_task_status(uname)
        elif choice == "4":
            delete_task(uname)
        elif choice == "5":
            print("Logged out successfully")
            break
        else:
            print("Invalid option")