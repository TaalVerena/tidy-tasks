# === IMPORTS ===
import gspread
import os
from google.oauth2.service_account import Credentials
from time import sleep

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
    notes = input("Enter task notes: \n")
    return description, category, priority, notes


def about_menu():
    """
    Displays the about menu for Tidy Tasks
    """
    clear_screen()
    print("Welcome to Tidy Tasks, your personal task management companion.\n")
    print("Crafted to bring simplicity and order to your daily to-dos.\n")
    print("\t- Easily view, add, edit, complete and remove tasks.\n")
    print("\t- Add a description, category, priority and notes to your task.\n")
    print("\t- Manage your tasks anywhere, any time at the click of a button.\n")
    
    input("Press enter to return to the main menu and get started!\n")
    clear_screen()

# Task class to represent individual tasks with their properties and methods
class Task:
    def __init__(
                self, task_id, description, 
                category, priority, status,
                notes
                ):
        """
        Initialise a task
        """
        self.task_id = task_id
        self.description = description
        self.category = category
        self.priority = priority
        self.status = status
        self.notes = notes

    def __str__(self):
        """
        Returns a string representation of a task
        """
        return f"ID: {self.task_id}\t Description: {self.description}\t \
                Category: {self.category}\t Priority: {self.priority}\t \
                Status: {self.status}\t Notes: {self.notes}"


# TaskManager class to manage various operations on
# tasks using the Google Sheets backend
class TaskManager:
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

        # Header
        headers = [
                    "task_id", "description", "category",
                    "priority", "status", "notes"
                    ]
        header_widths = []
        for header in headers:
            max_length = max(
                [len(str(getattr(task, header.lower()))) for task in tasks]
            )
            header_widths.append(max(max_length, len(header)))

        for i, header in enumerate(headers):
            print(header.ljust(header_widths[i]), end=" | ")
        print("\n" + "-" * (sum(header_widths) + len(headers) * 3 - 1))

        # Tasks
        for task in tasks:
            print(str(task.task_id).rjust(header_widths[0]), end=" | ")
            print(task.description.ljust(header_widths[1]), end=" | ")
            print(task.category.ljust(header_widths[2]), end=" | ")
            print(task.priority.ljust(header_widths[3]), end=" | ")
            print(task.status.ljust(header_widths[4]), end=" | ")
            print(task.notes.ljust(header_widths[5]))
        print("-" * (sum(header_widths) + len(headers) * 3 - 1))

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
        valid_priorities = ['high', 'medium', 'low']
        return priority.lower() in valid_priorities

    def add_task(self, description, category, priority, notes):
        """
        Adds a task to the spreadsheet after user confirmation
        """
        # Validate the priority
        if not self.validate_priority(priority):
            print("Priority must be high, medium, or low.")
            return

        # Display task details for confirmation
        while True:
            print("\nPlease confirm the task details:")
            print(f"Description: {description}")
            print(f"Category: {category}")
            print(f"Priority: {priority}")
            print(f"Notes: {notes}")
            confirmation = input("Add this task? (yes/no): ")

            if confirmation.lower() == 'yes':
                break
            else:
                print("\nTask not added.")
                decision = input("Would you like to re-enter the task details? (yes/no): ")
                if decision.lower() == 'yes':
                    description, category, priority, notes = get_task_info()
                    continue
                else:
                    print("Returning to the View and Manage Tasks menu...\n")
                    sleep(1.5)
                    return
        
        tasks_worksheet = self.sheet.worksheet("tasks")
        complete_worksheet = self.sheet.worksheet("complete")

        # Fetch tasks from both worksheets
        tasks_records = tasks_worksheet.get_all_records()
        complete_records = complete_worksheet.get_all_records()

        # Extract task IDs and convert them to integers
        task_ids = [
            int(record['task_id']) 
            for record in tasks_records + complete_records
        ]

        # Determine the next task ID (highest existing ID + 1)
        next_task_id = max(task_ids) + 1 if task_ids else 1

        # Add the new task
        tasks_worksheet.append_row([
            next_task_id, description, category,
            priority, "open", notes
        ])
        print("\nTask added successfully!")
        return

    def mark_task_as_complete(self):
        """
        Marks a task as complete, moves it to the complete tab
        and removes it from the tasks tab.
        """
        # 1. Get the row of the task to mark as complete
        try:
            task_id = int(
                            input((
                                "\nEnter the task ID you would like "
                                "to mark as complete:  \n"))
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
            task_to_complete.notes,
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

        choice = input((
                        "\nPress enter to return to the "
                        "main menu or 'q' to quit: \n"
                        ))
        if choice.lower() == "q":
            exit()
        else:
            clear_screen()

    def view_and_manage_tasks():
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
            print("5. Return to Main Menu")
            choice = input("Select an option: \n")

            if choice == "1":
                task_manager.add_task(*get_task_info())
            elif choice == "2":
                task_manager.edit_task()
            elif choice == "3":
                task_manager.mark_task_as_complete()
            elif choice == "4":
                print("Remove feature not yet implemented.")  # Placeholder
            elif choice == "5":
                clear_screen()
                main_menu()
                break
            else:
                print("Please select a valid option!\n")

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
        for task in tasks:
            if task.task_id == task_id:
                task_to_edit = task
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
        print("4. Notes")
        print("5. Status")
        choice = input("Enter your choice:  \n")

        new_value = input("\nEnter the new value:  \n")

        if choice == "1":
            task_to_edit.description = new_value
        elif choice == "2":
            task_to_edit.category = new_value
        elif choice == "3":
            task_to_edit.priority = new_value
        elif choice == "4":
            task_to_edit.notes = new_value
        elif choice == "5":
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
            task_to_edit.notes,
        ]

        range_start = "A{}".format(task_id + 1)
        range_end = "F{}".format(task_id + 1)
        cell_range = "{}:{}".format(range_start, range_end)
        cells = worksheet.range(cell_range)

        for cell, value in zip(cells, row_to_edit):
            cell.value = value

        worksheet.update_cells(cells)

        # Fetch updated task data
        updated_record = worksheet.row_values(task_id + 1)
        updated_task = Task(*updated_record)

        # Display the updated task to the user
        print("\nTask updated successfully!")
        print(updated_task)

        # Give the user the option to return to the main menu
        choice = input((
                        "\nPress enter to return to the "
                        "main menu or 'q' to quit: \n"
                        ))
        if choice.lower() == "q":
            exit()
        else:
            clear_screen()


# Initialize the TaskManager with the opened Google Sheets spreadsheet
task_manager = TaskManager(SHEET)


def main_menu():
    """
    Displays main menu for Tidy Tasks and handles user input / interaction
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
            TaskManager.view_and_manage_tasks()
        elif user_choice == "2":
            about_menu()
        elif user_choice == "3":
            exit()
        else:
            print("Please enter a valid option\n")

# Invoke the main menu to start the application
main_menu()
