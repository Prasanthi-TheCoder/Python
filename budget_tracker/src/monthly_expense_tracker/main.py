import argparse
from .add_expenses import add_expenses
from .view_expenses import view_expenses
from .load_expenses import load_expenses
from .add_expenses import add_expenses
from .track_budget import calculate_total_expenses

def show_help() ->None:
    """
    Function to show help message
    :return: None
    """
    print("""
                   Monthly Expense Tracker
                   Options:
                   -a, --add       Add a new expense
                   -v, --view      View expenses
                   -b, --budget    Track budget
                   -s, --save      Save expenses
                   """
          )


def main() ->None:
    """
    Main function
    :return: None
    """
    parser = argparse.ArgumentParser(
            description="Monthly Expense Tracker"
    )

    parser.add_argument(
       "-a",
        "--add",
        action="store_true",
        help="Add a new expense to CSV file"
    )

    parser.add_argument(
       "-v",
        "--view",
        action="store_true",
        help="View expenses"
    )

    parser.add_argument(
       "-b",
        "--budget",
        action="store_true",
        help="Track budget"
    )

    parser.add_argument(
        "-l",
        "--load",
        action="store_true",
        help="Load expenses from CSV file"
    )

    args = parser.parse_args()

    if args.add:
       add_expenses()
    elif args.view:
       view_expenses()
    elif args.budget:
       calculate_total_expenses()
    elif args.load:
       load_expenses()
    else:
        show_help()




if __name__ == '__main__':
    """
        Run the Budget Tracker application.
        Displays the main menu and handles user interactions
    """
    main()


