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
        input("\nPress enter to return to the main menu")
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
            description = input("Enter task description: \n")
            category = input("Enter task category: \n")
            priority = input("Enter task priority: \n")
            notes = input("Enter task notes: \n")
            task_manager.add_task(description, category, priority, notes)
            # Add error handling
        elif user_choice == "3":
            # help_menu()
            print(f"You have selected 3 {user_choice}\n")
        elif user_choice == "4":
            exit()
        else:
            print("Please enter a valid option\n")  

main_menu()