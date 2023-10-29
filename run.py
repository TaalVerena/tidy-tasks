import gspread
import os
from google.oauth2.service_account import Credentials



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("tidy_tasks")

def clear_screen():
    """
    Clears the terminal screen
    """
    os.system("cls" if os.name == "nt" else "clear")

def get_task_info():
    """
    Gets task information from the user
    """
    description = input("Enter task description: \n")
    category = input("Enter task category: \n")
    priority = input("Enter task priority: \n")
    notes = input("Enter task notes: \n")
    return description, category, priority, notes

class Task:
    def __init__(self, task_id, description, category, priority, status, notes):
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
        return f"ID: {self.task_id}\t Description: {self.description}\t Category: {self.category}\t Priority: {self.priority}\t Status: {self.status}\t Notes: {self.notes}"

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
        worksheet = self.sheet.worksheet("tasks")
        tasks = self.fetch_tasks()

        task_id = len(tasks) + 1
        worksheet.append_row([task_id, description, category, priority, 'Open', notes])
        print("\nTask added successfully!")
        input("\nPress enter to return to the main menu")
        clear_screen()
    
    def display_tasks(self):
        """
        Displays all tasks in the spreadsheet or
        a message if there are no tasks
        """
        tasks = self.fetch_tasks()
        if not tasks:
            print("No tasks found!")
            return

        for task in tasks:
            print(task)
        
        self.task_options()

        input("\nPress enter to return to the main menu")
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
        
        choice = input("\nSelect an option: ")

        if choice == "1":
            task_manager.add_task(*get_task_info())
        elif choice == "2":
            self.edit_task()
        elif choice == "3":
            # Placeholder for marking tasks as complete
            print("Mark as complete feature not yet implemented.")
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
            task_id = int(input("\nEnter the task ID you would like to edit: "))
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
        choice = input("Enter your choice: ")

        new_value = input("\nEnter the new value: ")

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
        row_to_edit = [task_to_edit.task_id, task_to_edit.description, task_to_edit.category, task_to_edit.priority, task_to_edit.status, task_to_edit.notes]
        worksheet.update(range_name='A{}:F{}'.format(task_id + 1, task_id + 1), values=[row_to_edit])

        # Fetch updated task data
        updated_record = worksheet.row_values(task_id + 1)
        updated_task = Task(*updated_record)

        # Display the updated task to the user
        print("\nTask updated successfully!")
        print(updated_task)

        # Give the user the option to return to the main menu
        choice = input("\nPress enter to return to the main menu or 'q' to quit: ")
        if choice.lower() == 'q':
            exit()
        else:
            clear_screen()

task_manager = TaskManager(SHEET)

def main_menu():
    """
    Displays main menu for Tidy Tasks
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
            # help_menu()
            print(f"You have selected 3 {user_choice}\n")
        elif user_choice == "4":
            exit()
        else:
            print("Please enter a valid option\n")  

main_menu()