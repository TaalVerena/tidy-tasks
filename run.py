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
    priority = input("Enter task priority: \n")
    notes = input("Enter task notes: \n")
    return description, category, priority, notes


def help_menu():
    """
    Displays the help menu for Tidy Tasks
    """
    clear_screen()
    print("Tidy Tasks Help Menu\n")
    print("Welcome to Tidy Tasks, your simple task management system!")
    print("Below you'll find detailed descriptions of each feature.\n")

    print("1. View tasks")
    print("\t- Displays all your current tasks along with their details (description, category, priority, status, and notes.)")

    print("2. Create a task")
    print("\t- Allows you to add a new task. You'll be prompted to enter details such as the task's description, category, priority, and any additional notes.")
    
    print("3. Edit a task")
    print("\t- Enables you to update the details of an existing task. Simply enter the task ID of the task you wish to edit, and follow the prompts to change the task's description, category, priority, status, or notes.")
    
    print("4. Mark a task as complete")
    print("\t- Mark a task as complete by entering its task ID. Completed tasks will be moved to a separate 'complete' tab.")
    
    print("5. Remove a task")
    print("\t- This allows you to delete a task permanently.")
    
    print("6. Help")
    print("\t- Displays this help menu with information about all the features and how to use them.")
    
    print("7. Exit")
    print("\t- Exits the application. All your tasks are saved in the spreadsheet and will be there when you come back!\n")
    
    input("Press enter to return to the main menu.\n")
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

    def add_task(self, description, category, priority, notes):
        """
        Adds a task to the spreadsheet
        """
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
            priority, "Open", notes
        ])
        print("\nTask added successfully!")
        return

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

        self.task_options()

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

    def task_options(self):
        """
        Displays the task options menu
        """
        print("\nTask Options:")
        print("1. Add a new task")
        print("2. Edit a task")
        print("3. Mark a task as complete")
        print("4. Remove a task")
        print("5. Return to main menu")

        choice = input("\nSelect an option:  \n")

        if choice == "1":
            task_manager.add_task(*get_task_info())
        elif choice == "2":
            self.edit_task()
        elif choice == "3":
            self.mark_task_as_complete()
        elif choice == "4":
            # Placeholder for removing tasks
            print("Remove feature not yet implemented.")
        elif choice == "5":
            clear_screen()
            return
        else:
            print("Please select a valid option!")
            self.task_options()

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
    while True:
        print("Welcome to Tidy Tasks\n")
        print("Please select an option:")
        print("1. View tasks")
        print("2. Create a task")
        print("3. Help")
        print("4. Exit\n")
        user_choice = input("Enter your choice: \n")

        if user_choice == "1":
            print("Retrieving list of tasks...\n")
            task_manager.display_tasks()
        elif user_choice == "2":
            task_manager.add_task(*get_task_info())
            # Add error handling
        elif user_choice == "3":
            help_menu()
        elif user_choice == "4":
            exit()
        else:
            print("Please enter a valid option\n")


# Invoke the main menu to start the application
main_menu()
