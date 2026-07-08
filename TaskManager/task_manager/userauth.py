import json
import hashlib
from typing import Any
import getpass
from .config import FILE_PATH
from .task_menu import menu



def save_users(users: dict[str, Any]) -> None:
    """
    Save the users to the list of users
    :param users: [dict[str, Any]]
    :return: None
    """
    try:
        with open(FILE_PATH, "w") as f:
           json.dump(users, f, indent=4)
    except FileNotFoundError as fe:
        print("Error saving users: {fe}")
        users ={}
    except json.decoder.JSONDecodeError as je:
        print("Error saving users: {je}")



def load_users() -> dict[str, Any]:
    """
    Load the users from the users file and
    dumps into the json file
    :return: dict[str, Any] - users
    """
    try:
        with open(FILE_PATH, "r") as f:
            users = json.load(f)
        if not users:
            print("No users found")
            users = {}
    except FileNotFoundError as fe:
        users ={}
    except json.decoder.JSONDecodeError as je:
        print("Error loading users: {je}")
        users ={}
    finally:
        return users



def registration() -> None:
    """
    Register a new user
    :return: None
    """
    users: dict[str, Any] = load_users()

    username = input("Username: ")
    if username.upper() in users:
        print(f"User {username} already exists")
        return

    password = getpass.getpass("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username.upper()] = {
        "password": hashed_password
    }

    save_users(users)
    print(f"User {username} successfully registered")


def login() -> None:
    """
    Login to the user
    :return:
    """

    users: dict[str, Any] = load_users()
    username = input("Username: ")
    if username.upper() not in users:
        print(f"User {username} does not exists in the database!!")
        return
    password = getpass.getpass("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if users[username.upper()]["password"] == hashed_password:
        print(f"User {username} logged in")
        menu(username)
    else:
        print(f"Invalid credentials!!")


