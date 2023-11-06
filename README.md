# Tidy Tasks
Welcome to Tidy Tasks, a personal to-do list app built with Python and Google Sheets.

## Introduction
Tidy Tasks is designed to help you keep track of your to-dos by adding, editing removing and marking tasks as complete.

## Live App
The live Tidy Tasks app can be found [here](https://tidy-tasks-9ed489f18853.herokuapp.com/).

![Tidy Tasks Homepage](README-media/tidy-tasks-homepage.png)

## Table of Contents

## User Experience (UX)
### Who Tidy Tasks Caters For
- Tidy Tasks is designed for anyone who wants to keep track of their to-dos. It is designed to be simple and easy to use, with a minimal homepage and a clean interface.
- Whether you're a busy parent, a student, or a professional, Tidy Tasks can help you keep track of your tasks.

### User Stories
| User Want or Need      | How It Is Achieved | Achieved |
| ----------- | ----------- | ----------- |
| Easily see what Tidy tasks is for      | An About section provides information about Tidy Tasks and what the user can achieve       | Yes       |
| Navigate the app with ease      | Numbered options with clear details present throughout       | Yes       |
| Manage tasks in one place     | A view and manage tasks section present with options for managing and viewing tasks       | Yes       |
| Add tasks easily     | A form with a text input and submit button is present       | Yes       |

## App Overview


## Planning
### Flowchart / Diagram

![Tidy Tasks Flowchart](README-media/tidy-tasks-flowchart.png)

### Color Scheme & Ascii Art
#### Color Scheme
- The colors throughout the application are kept minimal to ensure all text is easily readable.
- The ascii art is magenta to add a splash of color to the homepage and about page.
- Throughout the application, majority of the text is white on a black background.
- Menu options are magenta and table headers are blue to stand out from the rest of the text.
- Text inputs / prompts are green to ensure the user can easily identify where to input text.
- Error messages are red to ensure the user can easily identify when an error has occurred and successfully completed operations are green for user confirmation.

#### Ascii Art
- Homepage Ascii Art
    
    ![Homepage Ascii Art](README-media/homepage-ascii-art.png)

- About Ascii Art
    
    ![About Ascii Art](README-media/about-ascii-art.png)

## Features
### Existing Features
#### Homepage
- The homepage is minimal, inviting the user to navigate the app.
- Pops of color are used to draw the user's attention to the menu options and input.

    ![Homepage](README-media/tidy-tasks-homepage.png)  
##### Menu Options
1. View & Manage Tasks - This allows the user to view and manage their tasks.
2. About - This provides the user with information about Tidy Tasks.
3. Exit - This allows the user to exit the application and provides confirmation once selected.

#### View & Manage Tasks Menu
- By selecting option 1 from the homepage, the user is presented with the view and manage tasks menu.
- The user is presented with a table / list of their open tasks and a menu of options to manage their tasks.
- This differs from the flowchart in that viewing the list of tasks was originally intended to be one of the menu options. This change was implemented to make it easier for the user as they can now view their tasks without having to select an option from the menu and can see the different options available while viewing their open tasks.

    ![View & Manage Tasks Menu](README-media/view-and-manage-tasks-menu.png)

#### Add Task

#### Edit Task

### Future Features to Implement

## Testing
### Tests & Results
### Bugs
#### Fixed Bugs
#### Unfixed Bugs

## Deployment

## Credits
- Flowchart / diagram created using [Lucid Charts](https://www.lucidchart.com/pages/)
- Ascii Art created using [Patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

## Technologies Used
- **Python:** The primary programming language used to create the application logic.
- **Google Sheets API:** For storing and retrieving task data from a spreadsheet, serving as a database.
- **Colorama:** To enhance the CLI experience with colored text for better readability.
- **GSpread:** A Python API for Google Sheets used for operations on the spreadsheet.