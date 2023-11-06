# === IMPORTS ===
import gspread
import os
from google.oauth2.service_account import Credentials
from time import sleep
from tabulate import tabulate
from colorama import Fore, Style, init
init(autoreset=True)

# === GOOGLE SPREADSHEET AUTHENTICATION ===
# The necessary scopes to interact with Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Load credentials from the provided JSON file
CREDS = Credentials.from_service_account_file("creds.json")
# Assign the necessary scopes to the credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# Authorize and initialize the gspread client with the scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# Open the 'tidy_tasks' spreadsheet
SHEET = GSPREAD_CLIENT.open("tidy_tasks")

# ASCII art for Tidy Tasks homepage
tidy_tasks_ascii_art = r"""
  _______ _     _         _______        _
 |__   __(_)   | |       |__   __|      | |
    | |   _  __| |_   _     | | __ _ ___| | _____
    | |  | |/ _` | | | |    | |/ _` / __| |/ / __|
    | |  | | (_| | |_| |    | | (_| \__ \   <\__ \
    |_|  |_|\__,_|\__, |    |_|\__,_|___/_|\_\___/
                   __/ |
                  |___/
"""

# ASCII art for Tidy Tasks about page
about_ascii_art = r"""
           _                 _     _____        __
     /\   | |               | |   |_   _|      / _|       _
    /  \  | |__   ___  _   _| |_    | |  _ __ | |_ ___   (_)
   / /\ \ | '_ \ / _ \| | | | __|   | | | '_ \|  _/ _ \
  / ____ \| |_) | (_) | |_| | |_   _| |_| | | | || (_) |  _
 /_/    \_|_.__/ \___/ \__,_|\__| |_____|_| |_|_| \___/  (_)
"""


def print_ascii_art():
    """
    Prints the Tidy Tasks ASCII art in magenta
    """
    print(Fore.LIGHTMAGENTA_EX + tidy_tasks_ascii_art + Style.RESET_ALL)


def print_about_ascii_art():
    """
    Prints the Tidy Tasks about ASCII art in meganta
    """
    print(Fore.LIGHTMAGENTA_EX + about_ascii_art + Style.RESET_ALL)


def clear_screen():
    """
    Clears the terminal screen
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


def invalid_input():
    """
    Displays an invalid input message
    """
    sleep(1.5)
    print(
        Fore.RED + "\nInvalid input, please try again.\n" +
        Style.RESET_ALL
    )
    sleep(2)


def invalid_menu_option():
    """
    Displays an invalid menu option message
    """
    sleep(1.5)
    print(
        (
            Fore.RED + "\nInvalid input. " + Style.RESET_ALL +
            "Returning to the menu...\n"
        )
    )
    sleep(1.5)
    print(
        Fore.LIGHTGREEN_EX +
        "Please select one of the menu options listed.\n" + Style.RESET_ALL
    )
    sleep(2)
    clear_screen()


def id_not_found():
    """
    Displays an ID not found message
    """
    sleep(1.5)
    print(
        (
            Fore.RED + "\nNo task found with that id. " +
            Style.RESET_ALL + "Please try again. \n"
        )
    )


def get_non_empty_input(prompt):
    """
    Ensures that the user enters a non-empty input
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print(
                (Fore.RED + "Description cannot be empty."
                 "Please enter a valid description.\n" +
                 Style.RESET_ALL)
            )


def exit_tidy_tasks():
    """
    Exits the Tidy Tasks application
    """
    sleep(1.5)
    print(
        (
            Fore.LIGHTMAGENTA_EX +
            "\nThank you for using Tidy Tasks! Exiting application ...\n" +
            Style.RESET_ALL
        )
    )
    sleep(1.5)
    clear_screen()
    sleep(1.5)
    exit()


def return_to_main_menu():
    """
    Returns to the main menu
    """
    while True:
        choice = input(
            (
                Fore.LIGHTGREEN_EX +
                "\nPress enter to return to the main menu or 'q' to quit: \n" +
                Style.RESET_ALL
            )
        )
        if choice.lower() == "q":
            exit_tidy_tasks()
        elif choice.lower() == "":
            sleep(1.5)
            print("Returning to the main menu...\n")
            sleep(2)
            clear_screen()
            task_manager.view_and_manage_tasks()
        else:
            invalid_input()
            continue


def get_task_info():
    """
    Gets task information from the user
    """
    description = input(
        Fore.LIGHTGREEN_EX + "Enter task description: \n" +
        Style.RESET_ALL
    )
    print("\nTask Category Options:")
    for index, category in enumerate(TaskManager.VALID_CATEGORIES, start=1):
        print(
            Fore.LIGHTMAGENTA_EX +
            str(index) + ". " + Style.RESET_ALL + category
        )
    category_index = TaskManager.get_user_input(
        Fore.LIGHTGREEN_EX + "\nChoose a category " +
        Fore.LIGHTMAGENTA_EX + "(1 - 5): \n" + Style.RESET_ALL,
        TaskManager.validate_category
    )
    category = list(TaskManager.VALID_CATEGORIES)[int(category_index) - 1]

    print("\nTask Priority Options:")
    for index, priority in enumerate(TaskManager.VALID_PRIORITIES, start=1):
        print(
            Fore.LIGHTMAGENTA_EX + str(index) + ". " +
            Style.RESET_ALL + priority
        )
    priority_index = TaskManager.get_user_input(
        Fore.LIGHTGREEN_EX + "\nChoose a priority " + Fore.LIGHTMAGENTA_EX +
        "(1 - 3): \n" + Style.RESET_ALL, TaskManager.validate_priority
    )
    priority = TaskManager.VALID_PRIORITIES[int(priority_index) - 1]
    return description, category, priority


def about_menu():
    """
    Displays the about menu for Tidy Tasks
    """
    clear_screen()
    print_about_ascii_art()
    print("Welcome to Tidy Tasks, your personal task management companion.\n")
    print("Crafted to bring simplicity and order to your daily to-dos.\n")
    print(
        (Fore.LIGHTMAGENTA_EX + "\t- " + Style.RESET_ALL +
         "Easily view, add, edit, complete and remove tasks.\n")
    )
    print(
        (Fore.LIGHTMAGENTA_EX + "\t- " + Style.RESET_ALL +
         "Add a description, category and priority to your tasks.\n")
    )
    print(
        (Fore.LIGHTMAGENTA_EX + "\t- " + Style.RESET_ALL +
         "Manage your tasks anywhere, any time at the click of a button.\n")
    )

    input("Press enter to return to the homepage and get started!\n")
    clear_screen()


class Task:
    """
    Represents a task with its properties and methods
    """

    def __init__(self, task_id, description, category, priority, status):
        """
        Initialise a task
        """
        self.task_id = task_id
        self.description = description
        self.category = category
        self.priority = priority
        self.status = status

    def __str__(self):
        """
        Returns a string representation of a task
        """
        return f"ID: {self.task_id}\t Description: {self.description}\t \
                Category: {self.category}\t Priority: {self.priority}\t \
                Status: {self.status}"


class TaskManager:
    """
    Manages various operations on tasks using the Google Sheets backend
    """
    TASKS_SHEET_NAME = "tasks"
    COMPLETE_SHEET_NAME = "complete"
    VALID_CATEGORIES = {'home', 'work', 'studies', 'hobbies', 'exercise'}
    VALID_PRIORITIES = ['high', 'medium', 'low']

    def __init__(self, sheet):
        """
        Initialise the TaskManager class
        """
        self.sheet = sheet

    def fetch_tasks(self):
        """
        Fetches all tasks from the spreadsheet
        """
        worksheet = self.sheet.worksheet("tasks")
        records = worksheet.get_all_records()
        return [Task(**record) for record in records]

    def display_tasks(self):
        """
        Displays all tasks in the spreadsheet or
        a message if there are no tasks
        """
        tasks = self.fetch_tasks()
        if not tasks:
            print("No tasks found!")
            return

        # Preparing data for tabulate
        tasks_table = [
            [
                task.task_id, task.description,
                task.category, task.priority, task.status
            ]
            for task in tasks
        ]

        # Header
        headers = [
            Fore.BLUE + "Task ID" + Style.RESET_ALL,
            Fore.BLUE + "Description" + Style.RESET_ALL,
            Fore.BLUE + "Category" + Style.RESET_ALL,
            Fore.BLUE + "Priority" + Style.RESET_ALL,
            Fore.BLUE + "Status" + Style.RESET_ALL
        ]

        # Using tabulate to print a neat table
        print(tabulate(tasks_table, headers=headers, tablefmt="fancy_grid"))

        return

    def display_completed_tasks(self):
        """
        Displays all completed tasks in the spreadsheet or
        a message if there are no completed tasks
        """
        worksheet = self.sheet.worksheet("complete")
        records = worksheet.get_all_records()
        completed_tasks = [Task(**record) for record in records]

        if not completed_tasks:
            sleep(1.5)
            print("No completed tasks found!")
            sleep(2)
            return

        print("\nCompleted Tasks:\n")

        # Preparing data for tabulate
        headers = [
            Fore.BLUE + "Task ID" + Style.RESET_ALL,
            Fore.BLUE + "Description" + Style.RESET_ALL,
            Fore.BLUE + "Category" + Style.RESET_ALL,
            Fore.BLUE + "Priority" + Style.RESET_ALL,
            Fore.BLUE + "Status" + Style.RESET_ALL
        ]
        tasks_table = [
            [getattr(task, header.replace(" ", "_").lower())
             for header in headers] for task in completed_tasks
        ]
        print(tabulate(tasks_table, headers=headers, tablefmt="fancy_grid"))

        return_to_main_menu()

    @staticmethod
    def get_user_input(prompt, validation_func=None):
        """
        Repeatedly asks for user input until valid data is provided.
        """
        while True:
            data = input(prompt)
            if not validation_func or validation_func(data):
                return data
            invalid_input()
            continue

    @staticmethod
    def validate_priority(index):
        """
        Validates the task priority index
        """
        try:
            int_index = int(index)
            return 1 <= int_index <= len(TaskManager.VALID_PRIORITIES)
        except ValueError:
            return False

    @staticmethod
    def validate_category(index):
        """
        Validates the task category index
        """
        try:
            int_index = int(index)
            return 1 <= int_index <= len(TaskManager.VALID_CATEGORIES)
        except ValueError:
            return False

    def add_task(self, description, category, priority):
        # Display task details for confirmation
        while True:
            clear_screen()
            print("\nPlease confirm the task details: \n")
            print(f"Description: {description}")
            print(f"Category: {category}")
            print(f"Priority: {priority}")
            confirmation = input(
                Fore.LIGHTGREEN_EX + "\nAdd this task? (yes/no): " +
                Style.RESET_ALL
            )

            if confirmation.lower() == "yes":
                break
            elif confirmation.lower() == "no":
                print(Fore.RED + "\nTask not added." + Style.RESET_ALL)
                decision = input(
                    Fore.LIGHTGREEN_EX +
                    "\nWould you like to re-enter the task details? (yes/no): "
                    + Style.RESET_ALL
                )
                if decision.lower() == "yes":
                    clear_screen()
                    description, category, priority = get_task_info()
                    continue
                else:
                    print("\nReturning to the View and Manage Tasks menu...\n")
                    sleep(2)
                    clear_screen()
                    return
            else:
                invalid_input()
                continue

        tasks_worksheet = self.sheet.worksheet("tasks")
        complete_worksheet = self.sheet.worksheet("complete")

        # Fetch tasks from both worksheets
        tasks_records = tasks_worksheet.get_all_values()[1:]
        complete_records = complete_worksheet.get_all_values()[1:]

        # Check if there are records in both worksheets
        if tasks_records or complete_records:
            # Extract task IDs and convert them to integers
            task_ids = [int(record[0]) for record in tasks_records]
            if complete_records:
                task_ids.extend(
                    [int(record[0]) for record in complete_records]
                )
            # Determine the next task ID (highest existing ID + 1)
            next_task_id = max(task_ids) + 1
        else:
            # If both are empty, start with task ID 1
            next_task_id = 1

        # Add the new task
        tasks_worksheet.append_row(
            [next_task_id, description, category, priority, "open"]
        )
        print(
            Fore.LIGHTGREEN_EX + "\nTask added successfully! \n" +
            Style.RESET_ALL
        )
        sleep(1.5)
        print("Returning to the View and Manage Tasks menu...\n")
        sleep(2)
        clear_screen()
        return

    def mark_task_as_complete(self):
        """
        Marks a task as complete, moves it to the complete tab
        and removes it from the tasks tab.
        """
        # 1. Get the row of the task to mark as complete
        try:
            task_id = int(
                input(
                    (
                        Fore.LIGHTGREEN_EX + "\nEnter the task ID " +
                        "you would like to mark as complete: " +
                        Style.RESET_ALL
                    )
                )
            )
        except ValueError:
            invalid_input()
            return

        tasks = self.fetch_tasks()
        task_to_complete = None
        row_index = None
        for index, task in enumerate(tasks, start=2):
            if task.task_id == task_id:
                task_to_complete = task
                row_index = index
                break

        if not task_to_complete:
            id_not_found()
            TaskManager.mark_task_as_complete(self)
            return

        # Display task details and confirm completion
        clear_screen()
        print("\nTask Details:\n")
        print(f"Description: {task_to_complete.description}")
        print(f"Category: {task_to_complete.category}")
        print(f"Priority: {task_to_complete.priority}")
        confirmation = input(
            Fore.LIGHTGREEN_EX + "\nMark this task as complete? (yes/no): " +
            Style.RESET_ALL
        )

        if confirmation.lower() != "yes":
            print(
                Fore.RED + "\nTask not marked as complete." +
                Style.RESET_ALL
            )
            sleep(2)
            return

        print(f"\nMarking task with ID {task_id} as complete...\n")
        task_to_complete.status = "complete"
        sleep(2)

        # 2. Move task to the complete tab in Google Sheets
        complete_worksheet = self.sheet.worksheet("complete")
        row_to_append = [
            task_to_complete.task_id,
            task_to_complete.description,
            task_to_complete.category,
            task_to_complete.priority,
            task_to_complete.status,
        ]
        complete_worksheet.append_row(row_to_append)
        print(f"Task with ID {task_id} moved to the complete tab.\n")

        # 3. Remove completed task from the tasks tab in Google Sheets
        tasks_worksheet = self.sheet.worksheet("tasks")
        if row_index:
            tasks_worksheet.delete_rows(row_index)
            sleep(2)
            print(f"Task with ID {task_id} removed from the tasks tab.")
        else:
            print("Unable to find the task in the sheet to delete.")

        sleep(2)

        return_to_main_menu()

    def edit_task(self):
        """
        Edits an existing task in the spreadsheet
        """
        while True:
            try:
                task_id = int(input
                              (
                                (Fore.LIGHTGREEN_EX +
                                 "\nEnter the task ID you would like to edit: "
                                 + Style.RESET_ALL)
                                ))
                tasks = self.fetch_tasks()
                task_to_edit = None
                row_index = None
                for index, task in enumerate(tasks, start=2):
                    if task.task_id == task_id:
                        task_to_edit = task
                        row_index = index
                        break

                if not task_to_edit:
                    id_not_found()
                    continue

                while True:
                    clear_screen()
                    print("\nCurrent Task Details:\n")
                    print(f"Description: {task_to_edit.description}")
                    print(f"Category: {task_to_edit.category}")
                    print(f"Priority: {task_to_edit.priority}")

                    print("\nWhich field would you like to edit?")
                    print(
                        Fore.LIGHTMAGENTA_EX + "1. " + Style.RESET_ALL +
                        "Description"
                    )
                    print(
                        Fore.LIGHTMAGENTA_EX + "2. " + Style.RESET_ALL +
                        "Category"
                    )
                    print(
                        Fore.LIGHTMAGENTA_EX + "3. " + Style.RESET_ALL +
                        "Priority"
                    )
                    choice = input(
                        Fore.LIGHTGREEN_EX + "\nEnter your choice: \n" +
                        Style.RESET_ALL
                    )

                    if choice == "1":
                        new_value = get_non_empty_input(
                            (
                                Fore.LIGHTGREEN_EX +
                                "\nEnter a new description: \n" +
                                Style.RESET_ALL
                            )
                        )
                        task_to_edit.description = new_value
                    elif choice == "2":
                        print("\nTask Category Options:")
                        for index, category in enumerate(
                                TaskManager.VALID_CATEGORIES, start=1):
                            print(
                                Fore.LIGHTMAGENTA_EX + str(index) + ". " +
                                Style.RESET_ALL + category
                            )
                        category_index = TaskManager.get_user_input(
                            Fore.LIGHTGREEN_EX + "\nChoose a new category " +
                            Fore.LIGHTMAGENTA_EX + "(1 - 5): \n" +
                            Style.RESET_ALL, TaskManager.validate_category
                        )
                        new_value = list(TaskManager.VALID_CATEGORIES)[
                            int(category_index) - 1
                        ]
                        task_to_edit.category = new_value
                    elif choice == "3":
                        print("\nTask Priority Options:")
                        for index, priority in enumerate(
                                TaskManager.VALID_PRIORITIES, start=1):
                            print(
                                Fore.LIGHTMAGENTA_EX + str(index) + ". " +
                                Style.RESET_ALL + priority
                            )
                        priority_index = TaskManager.get_user_input(
                            Fore.LIGHTGREEN_EX + "\nChoose a new priority " +
                            Fore.LIGHTMAGENTA_EX + "(1 - 3): \n" +
                            Style.RESET_ALL, TaskManager.validate_priority
                        )
                        new_value = TaskManager.VALID_PRIORITIES[
                            int(priority_index) - 1
                        ]
                        task_to_edit.priority = new_value
                    else:
                        invalid_input()
                        continue

                    clear_screen()
                    print("\nPlease confirm the updated task details: \n")
                    print(f"Description: {task_to_edit.description}")
                    print(f"Category: {task_to_edit.category}")
                    print(f"Priority: {task_to_edit.priority}")
                    confirmation = input(
                        Fore.LIGHTGREEN_EX + "\nSave these changes? (yes/no): "
                        + Style.RESET_ALL
                    )

                    if confirmation.lower() == "yes":
                        break
                    elif confirmation.lower() == "no":
                        print(
                            Fore.RED + "\nChanges not saved." +
                            Style.RESET_ALL
                        )
                        decision = input(
                            Fore.LIGHTGREEN_EX +
                            "\nWould you like to re-edit the task? (yes/no): "
                            + Style.RESET_ALL
                        )
                        if decision.lower() == "yes":
                            continue
                        else:
                            print(
                                (
                                    "Returning to the "
                                    "View and Manage Tasks menu...\n"
                                )
                            )
                            sleep(2)
                            return
                    else:
                        invalid_input()
                        continue
                break

            except ValueError:
                print(
                    Fore.RED +
                    "\nInvalid input. Please enter a valid task ID." +
                    Style.RESET_ALL
                )
        worksheet = self.sheet.worksheet("tasks")
        row_to_edit = [
            task_to_edit.task_id,
            task_to_edit.description,
            task_to_edit.category,
            task_to_edit.priority,
            task_to_edit.status,
        ]

        worksheet.delete_rows(row_index)
        worksheet.insert_row(row_to_edit, row_index)

        print(
            Fore.LIGHTGREEN_EX + "\nTask updated successfully!" +
            Style.RESET_ALL
        )
        sleep(1.5)
        return_to_main_menu()

    def remove_task(self):
        """
        Removes an existing task from the spreadsheet
        """
        while True:
            try:
                task_id = int(input(
                    ("\nEnter the task ID you would like to remove: ")
                ))
            except ValueError:
                invalid_input()
                continue

            tasks = self.fetch_tasks()
            task_to_remove = None
            row_index = None
            for index, task in enumerate(tasks, start=2):
                if task.task_id == task_id:
                    task_to_remove = task
                    row_index = index
                    break

            if not task_to_remove:
                id_not_found()
                decision = input(
                    "Would you like to remove a different task? (yes/no): "
                )
                if decision.lower() == "yes":
                    continue
                else:
                    print("Returning to the View and Manage Tasks menu...\n")
                    sleep(2)
                    return

            print("\nTask to remove:")
            print(task_to_remove)

            while True:
                confirmation = input(
                    "Are you sure you want to remove this task? (yes/no): "
                )

                if confirmation.lower() == "yes":
                    worksheet = self.sheet.worksheet("tasks")
                    worksheet.delete_rows(row_index)
                    print("\nTask removed successfully!")
                    break
                elif confirmation.lower() == "no":
                    print("\nTask not removed.")
                    decision = input(
                        "Would you like to remove a different task? (yes/no): "
                    )
                    if decision.lower() == "yes":
                        break
                    else:
                        print(
                            "Returning to the View and Manage Tasks menu...\n"
                        )
                        sleep(2)
                        return
                else:
                    invalid_input()
                    continue

            return_to_main_menu()

    @staticmethod
    def view_and_manage_tasks():
        """
        Displays the task management sub-menu for Tidy Tasks
        """
        clear_screen()
        while True:
            print("\nTasks & Options:\n")
            task_manager.display_tasks()
            print((
                Fore.LIGHTMAGENTA_EX + "\n1. " +
                Style.RESET_ALL + "Add a new task"
            ))
            print((
                Fore.LIGHTMAGENTA_EX + "2. " +
                Style.RESET_ALL + "Edit a task"
            ))
            print((
                Fore.LIGHTMAGENTA_EX + "3. " +
                Style.RESET_ALL + "Mark a task as complete"
            ))
            print((
                Fore.LIGHTMAGENTA_EX + "4. " +
                Style.RESET_ALL + "Remove a task"
            ))
            print((
                Fore.LIGHTMAGENTA_EX + "5. " +
                Style.RESET_ALL + "View completed tasks"
            ))
            print((
                Fore.LIGHTMAGENTA_EX + "6. " +
                Style.RESET_ALL + "Return to homepage\n"
            ))
            choice = input(
                Fore.LIGHTGREEN_EX + "Enter your choice: " + Style.RESET_ALL
            )

            if choice == "1":
                clear_screen()
                description, category, priority = get_task_info()
                task_manager.add_task(description, category, priority)
            elif choice == "2":
                task_manager.edit_task()
            elif choice == "3":
                task_manager.mark_task_as_complete()
            elif choice == "4":
                task_manager.remove_task()
            elif choice == "5":
                clear_screen()
                task_manager.display_completed_tasks()
                break
            elif choice == "6":
                clear_screen()
                homepage()
                break
            else:
                invalid_menu_option()
                continue


# Initialize the TaskManager with the opened Google Sheets spreadsheet
task_manager = TaskManager(SHEET)


def homepage():
    """
    Displays homepage or landing page for Tidy Tasks
    and handles user input / interaction
    """
    clear_screen()
    while True:
        print_ascii_art()
        print(Fore.CYAN + "Welcome to Tidy Tasks!\n")
        print(Fore.LIGHTMAGENTA_EX + "Please select an option:")
        print((
            Fore.LIGHTMAGENTA_EX + "1." + Style.RESET_ALL +
            " View and manage tasks"
        ))
        print(Fore.LIGHTMAGENTA_EX + "2." + Style.RESET_ALL + " About")
        print(Fore.LIGHTMAGENTA_EX + "3." + Style.RESET_ALL + " Exit\n")
        user_choice = input(
            Fore.LIGHTGREEN_EX + "Enter your choice: " + Style.RESET_ALL
        )

        if user_choice == "1":
            clear_screen()
            TaskManager.view_and_manage_tasks()
        elif user_choice == "2":
            about_menu()
        elif user_choice == "3":
            exit_tidy_tasks()
        else:
            invalid_menu_option()
            continue


# Invoke the homepage / landing page to start the application
homepage()
