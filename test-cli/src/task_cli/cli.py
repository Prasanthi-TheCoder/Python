import click


from .tasks import (
    add_task,
    get_tasks,
    complete_task
)


@click.group()
def cli():
    "A simple CLI application for tasks"
    pass


@cli.command()
@click.argument("name")
def add(name):
    task = add_task(name)
    click.echo(f"Task created with task name : {task['name']}")


@cli.command("list")
def list_tasks():
    tasks = get_tasks()

    if not tasks:
        print(f"No tasks found")

    for task in tasks:
        click.echo(f"list: task name: {task['name']}")


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    task = complete_task(task_id)
    if task:
        click.echo(f"Completed task with id {task_id}")
    else:
        click.echo(f"No task with id {task_id}")

