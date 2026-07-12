tasks = []


def add_task(name):

    task = {
        "id": len(tasks) + 1,
        "name": name,
        "completed": False
    }

    tasks.append(task)
    return task


def get_tasks():
    for task in tasks:
        print(task)
    return tasks


def complete_task(task_id):

    for task in tasks:

        if task["id"] == task_id:
            task["completed"] = True
            return task

    return None