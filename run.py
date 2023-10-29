import gspread
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

class Task:
    def __init__(self, task_id, description, category, priority, status, notes):
        self.task_id = task_id
        self.description = description
        self.category = category
        self.priority = priority
        self.status = status
        self.notes = notes

    def __str__(self):
        return f"ID: {self.task_id}\t Description: {self.description}\t Category: {self.category}\t Priority: {self.priority}\t Status: {self.status}\t Notes: {self.notes}"

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
            print(f"You have selected 1 {user_choice}\n")
            view_tasks()
        elif user_choice == "2":
            # create_task()
            print(f"You have selected 2  {user_choice}\n")
        elif user_choice == "3":
            # help_menu()
            print(f"You have selected 3 {user_choice}\n")
        elif user_choice == "4":
            exit()
        else:
            print("Please enter a valid option\n")

def view_tasks():
    """
    Pulls information from Google Sheets and
    displays the to do list tasks
    """
    worksheet = SHEET.worksheet("tasks")
    tasks = worksheet.get_all_records()

    if not tasks:
        print("No tasks found!")
        return

    for task in tasks:
        print(
            f"Task ID: {task['Task ID']}\t Description: {task['Task Description']}\t Category: {task['Category']}\t Priority: {task['Priority']}\t Status: {task['Status']}\t Notes: {task['Notes']}"
        )

main_menu()