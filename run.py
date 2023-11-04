# === IMPORTS ===
import gspread
import os
from google.oauth2.service_account import Credentials
from time import sleep
from tabulate import tabulate

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


def clear_screen():
    """
    Clears the terminal screen
    """
    os.system("clear")


def return_to_main_menu():
    """
    Returns to the main menu
    """
    while True:
        choice = input(
            ("\nPress enter to return to the " "main menu or 'q' to quit: \n")
        )
        if choice.lower() == "q":
            sleep(1.5)
            print("Thank you for using Tidy Tasks!\n")
            sleep(1.5)
            exit()
        elif choice.lower() == "":
            sleep(1.5)
            print("Returning to the main menu...\n")
            sleep(1.5)
            clear_screen()
            return
        else:
            sleep(1.5)
            print("Invalid input, please try again.\n")
            sleep(1.5)
            continue


def get_task_info():
    """
    Gets task information from the user
    """
    description = input("Enter task description: \n")
    category = input("Enter task category: \n")
    priority = TaskManager.get_user_input(
        "Enter task priority (high, medium, low): \n",
        TaskManager.validate_priority
    )
    return description, category, priority


def about_menu():
    """
    Displays the about menu for Tidy Tasks
    """
    clear_screen()
    print("Welcome to Tidy Tasks, your personal task management companion.\n")
    print("Crafted to bring simplicity and order to your daily to-dos.\n")
    print("\t- Easily view, add, edit, complete and remove tasks.\n")
    print("\t- Add a description, category and priority to your tasks.\n")
    print((
        "\t- Manage your tasks anywhere,"
        " any time at the click of a button.\n"))

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
        headers = ["Task ID", "Description", "Category", "Priority", "Status"]

        # Using tabulate to print a neat table
        print(tabulate(tasks_table, headers=headers, tablefmt="fancy_grid"))

        return

    @staticmethod
    def get_user_input(prompt, validation_func=None):
        """
        Repeatedly asks for user input until valid data is provided.
        """
        while True:
            data = input(prompt)
            if not validation_func or validation_func(data):
                return data
            print("Invalid input, please try again.")

    @staticmethod
    def validate_priority(priority):
        """
        Validates the task priority
        """
        valid_priorities = ["high", "medium", "low"]
        return priority.lower() in valid_priorities

    def add_task(self, description, category, priority):
        """
        Adds a task to the spreadsheet after user confirmation
        """
        # Validate the priority
        if not self.validate_priority(priority):
            print("Priority must be high, medium, or low.")
            return

        # Display task details for confirmation
        while True:
            clear_screen()
            print("\nPlease confirm the task details: \n")
            print(f"Description: {description}")
            print(f"Category: {category}")
            print(f"Priority: {priority}")
            confirmation = input("Add this task? (yes/no): ")

            if confirmation.lower() == "yes":
                break
            elif confirmation.lower() == "no":
                print("\nTask not added.")
                decision = input(
                    "Would you like to re-enter the task details? (yes/no): "
                )
                if decision.lower() == "yes":
                    description, category, priority = get_task_info()
                    continue
                else:
                    print("Returning to the View and Manage Tasks menu...\n")
                    sleep(1.5)
                    return
            else:
                print("Invalid input, please try again.")
                continue

        tasks_worksheet = self.sheet.worksheet("tasks")
        complete_worksheet = self.sheet.worksheet("complete")

        # Fetch tasks from both worksheets
        tasks_records = tasks_worksheet.get_all_records()
        complete_records = complete_worksheet.get_all_records()

        # Extract task IDs and convert them to integers
        task_ids = [
            int(record["task_id"]) for record in
            tasks_records + complete_records
        ]

        # Determine the next task ID (highest existing ID + 1)
        next_task_id = max(task_ids) + 1 if task_ids else 1

        # Add the new task
        tasks_worksheet.append_row(
            [next_task_id, description, category, priority, "open"]
        )
        print("\nTask added successfully! \n")
        sleep(1.5)
        print("Returning to the View and Manage Tasks menu...\n")
        sleep(1.5)
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
                        "\nEnter the task ID you "
                        "would like to mark as complete: \n"
                    )
                )
            )
        except ValueError:
            print("Please enter a valid task ID.")
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
            print(f"No task found with ID {task_id}.")
            return

        print(f"\nMarking task with ID {task_id} as complete...\n")
        task_to_complete.status = "complete"
        sleep(1.5)

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
            sleep(1.5)
            print(f"Task with ID {task_id} removed from the tasks tab.")
        else:
            print("Unable to find the task in the sheet to delete.")

        sleep(1.5)

        return_to_main_menu()

    def edit_task(self):
        """
        Edits an existing task in the spreadsheet
        """
        try:
            task_id = int(input((
                "\nEnter the task ID you would like to edit: \n"
                )))
        except ValueError:
            print("Please enter a valid task ID.")
            return

        tasks = self.fetch_tasks()
        task_to_edit = None
        row_index = None
        for index, task in enumerate(tasks, start=2):
            if task.task_id == task_id:
                task_to_edit = task
                row_index = index
                break

        if not task_to_edit:
            print(f"No task found with ID {task_id}.")
            return

        print("\nCurrent task details:")
        print(task_to_edit)

        print("\nWhich field do you want to edit?")
        print("1. Description")
        print("2. Category")
        print("3. Priority")
        print("4. Status")
        choice = input("Enter your choice:  \n")

        new_value = input("\nEnter the new value:  \n")

        if choice == "1":
            task_to_edit.description = new_value
        elif choice == "2":
            task_to_edit.category = new_value
        elif choice == "3":
            task_to_edit.priority = new_value
        elif choice == "4":
            task_to_edit.status = new_value
        else:
            print("Invalid choice!")
            return

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

        print("\nTask updated successfully!")

        return_to_main_menu()

    def remove_task(self):
        """
        Removes an existing task from the spreadsheet
        """
        while True:
            try:
                task_id = int(input(
                    ("\nEnter the task ID you would like to remove: \n")
                ))
            except ValueError:
                print("Please enter a valid task ID.")
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
                print(f"No task found with ID {task_id}.")
                decision = input(
                    "Would you like to remove a different task? (yes/no): "
                )
                if decision.lower() == "yes":
                    continue
                else:
                    print("Returning to the View and Manage Tasks menu...\n")
                    sleep(1.5)
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
                        print("Returning to the View and Manage Tasks menu...\n")
                        sleep(1.5)
                        return
                else:
                    print("Invalid input, please try again.")

            return_to_main_menu()

    def view_and_manage_tasks(self):
        """
        Displays the task management sub-menu for Tidy Tasks
        """
        clear_screen()
        while True:
            print("\nView and Manage Tasks:\n")
            task_manager.display_tasks()
            print("1. Add a new task")
            print("2. Edit a task")
            print("3. Mark a task as complete")
            print("4. Remove a task")
            print("5. Return to home page\n")
            choice = input("Select an option: \n")

            if choice == "1":
                clear_screen()
                task_manager.add_task(*get_task_info())
            elif choice == "2":
                task_manager.edit_task()
            elif choice == "3":
                task_manager.mark_task_as_complete()
            elif choice == "4":
                task_manager.remove_task()
            elif choice == "5":
                clear_screen()
                homepage()
                break
            else:
                print("Please select a valid option!\n")


# Initialize the TaskManager with the opened Google Sheets spreadsheet
task_manager = TaskManager(SHEET)


def homepage():
    """
    Displays homepage or landing page for Tidy Tasks
    and handles user input / interaction
    """
    clear_screen()
    while True:
        print("Welcome to Tidy Tasks\n")
        print("Please select an option:")
        print("1. View and manage tasks")
        print("2. About")
        print("3. Exit\n")
        user_choice = input("Enter your choice: \n")

        if user_choice == "1":
            clear_screen()
            TaskManager.view_and_manage_tasks()
        elif user_choice == "2":
            about_menu()
        elif user_choice == "3":
            exit()
        else:
            print("Please enter a valid option\n")


# Invoke the homepage / landing page to start the application
homepage()
