import argparse
from .userauth import registration,login



def show_help() -> None:
    """
    Displays this help message
    :return: None
    """
    print("""
                      Task Manager
                      Options:
                      auth [-r | -l]      User authentication (registration/login)         
                      """
          )



def main() -> None:
    """
    Main function
    :return: None
    """

    parser = argparse.ArgumentParser(
        description=" Task Manager"
    )

    auth_parser = parser.add_argument_group(
        "Authentication"
    )

    auth_parser.add_argument(
        "auth",
        nargs="?",
        help="User authentication"
    )

    auth_options = parser.add_mutually_exclusive_group()

    auth_options.add_argument(
        "-r",
        "--register",
        action="store_true",
        help="Register a new user"
    )
    auth_options.add_argument(
        "-l",
        "--login",
        action="store_true",
        help="Login user"
    )

    args = parser.parse_args()

    if args.register:
        registration()
    elif args.login:
        login()
    else:
        show_help()



if __name__ == '__main__':
    main()