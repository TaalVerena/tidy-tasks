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

def main_menu():
    """
    Displays main menu for Tidy Tasks
    """
    print("Welcome to Tidy Tasks\n")
    print("Please select an option:")
    print("1. View To Do Lists")
    print("2. Create a To Do List")
    print("3. Help")
    print("4. Exit\n")
    user_choice = input("Enter your choice: \n")
    print(f"You have selected {user_choice}\n")

main_menu()