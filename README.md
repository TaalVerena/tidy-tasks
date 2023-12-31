# Tidy Tasks
Welcome to Tidy Tasks, a personal to-do list app.

## Introduction
Tidy Tasks is designed to help you keep track of your to-dos by adding, editing removing and marking tasks as complete.

## Live App
The live Tidy Tasks app can be found [here](https://tidy-tasks-9ed489f18853.herokuapp.com/).

![Tidy Tasks Homepage](README-media/tidy-tasks-homepage.png)

## Table of Contents
- [Tidy Tasks](#tidy-tasks)
  - [Introduction](#introduction)
  - [Live App](#live-app)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Who Tidy Tasks Caters For](#who-tidy-tasks-caters-for)
    - [User Stories](#user-stories)
  - [Planning](#planning)
    - [Flowchart / Diagram](#flowchart--diagram)
    - [Concept](#concept)
    - [Color Scheme \& Ascii Art](#color-scheme--ascii-art)
      - [Color Scheme](#color-scheme)
      - [Ascii Art](#ascii-art)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Homepage](#homepage)
        - [Menu Options](#menu-options)
      - [View \& Manage Tasks Menu](#view--manage-tasks-menu)
      - [Add Task](#add-task)
      - [Edit Task](#edit-task)
      - [Mark Task as Complete](#mark-task-as-complete)
      - [Remove Task](#remove-task)
      - [View Completed Tasks](#view-completed-tasks)
      - [About Section](#about-section)
    - [Future Features to Implement](#future-features-to-implement)
  - [Testing](#testing)
    - [Linter Testing](#linter-testing)
    - [Manual Testing](#manual-testing)
      - [Test 1: Homepage Navigation](#test-1-homepage-navigation)
      - [Test 2: Homepage - Error Handling](#test-2-homepage---error-handling)
      - [Test 3: View \& Manage Tasks Menu](#test-3-view--manage-tasks-menu)
      - [Test 4: View \& Manage Tasks Menu - Error Handling](#test-4-view--manage-tasks-menu---error-handling)
      - [Test 5: Add Task](#test-5-add-task)
      - [Test 6: Add Task - Error Handling](#test-6-add-task---error-handling)
      - [Test 7: Edit Task](#test-7-edit-task)
      - [Test 8: Edit Task - Error Handling](#test-8-edit-task---error-handling)
      - [Test 9: Mark Task as Complete](#test-9-mark-task-as-complete)
      - [Test 10: Mark Task as Complete - Error Handling](#test-10-mark-task-as-complete---error-handling)
      - [Test 11: Remove Task](#test-11-remove-task)
      - [Test 12: Remove Task - Error Handling](#test-12-remove-task---error-handling)
      - [Test 13: View Completed Tasks](#test-13-view-completed-tasks)
      - [Test 14: View Completed Tasks - Error Handling](#test-14-view-completed-tasks---error-handling)
      - [Test 15: About](#test-15-about)
    - [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning the GitHub Repository](#cloning-the-github-repository)
    - [APIs](#apis)
  - [Credits](#credits)
  - [Technologies Used](#technologies-used)

## User Experience (UX)
### Who Tidy Tasks Caters For
- Tidy Tasks is designed for anyone who wants to keep track of their to-dos. It is designed to be simple and easy to use, with a minimal homepage and a clean interface.
- Whether you're a busy parent, a student, or a professional, Tidy Tasks can help you keep track of your tasks in a simple, easy to use app.

### User Stories
| User Want or Need      | How It Is Achieved | Achieved |
| ----------- | ----------- | ----------- |
| Easily see what Tidy Tasks is for      | An About section provides information about Tidy Tasks and what the user can achieve through using Tidy Tasks       | Yes       |
| Navigate the app with ease      | Numbered options with clear details present throughout       | Yes       |
| Manage tasks in one place     | A view and manage tasks section present with options for managing and viewing tasks       | Yes       |
| Easily manage tasks     | A step by step process for adding, editing, removing and marking tasks as complete       | Yes       |

## Planning
### Flowchart / Diagram

![Tidy Tasks Flowchart](README-media/tidy-tasks-flowchart.png)

### Concept
- The concept for Tidy Tasks was to create a simple, easy to use to-do list app that allows the user to add, edit, remove and mark tasks as complete.
- The app is designed to be personalized and offers a minimal layout and a clean interface.
- Being able to access the app from anywhere was another key concept, which is why the app is hosted on Heroku and uses Google Sheets as a database.
- Having access to all tasks in a neat, easy to read table / list was a key feature of the app and has been implemented to ensure the user can easily view and manage their tasks.

### Color Scheme & Ascii Art
#### Color Scheme
- The colors throughout the application are kept minimal to ensure all text is easily readable.
- The ascii art is magenta to add a splash of color to the homepage and about page.
- Throughout the application, majority of the text is white on a black background.
- Menu options are magenta and table headers are blue to stand out from the rest of the text.
- Text inputs / prompts are green to ensure the user can easily identify where to input text / select an option.
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
1. **View & Manage Tasks** - This allows the user to view and manage their tasks.
2. **About** - This provides the user with information about Tidy Tasks.
3. **Exit** - This allows the user to exit the application and provides confirmation once selected.

#### View & Manage Tasks Menu
- By selecting option 1 from the homepage, the user is presented with the view and manage tasks menu.
- The user is presented with a table / list of their open tasks and a menu of options to manage their tasks.
- This differs from the flowchart in that viewing the list of tasks was originally intended to be one of the menu options. This change was implemented to make it easier for the user as they can now view their tasks without having to select an option from the menu and can see the different options available while viewing their open tasks.

    ![View & Manage Tasks Menu](README-media/view-and-manage-tasks-menu.png)
- If there are no tasks, the user is presented with a message confirming there are no open tasks.
  
    ![No Open Tasks](README-media/no-open-tasks.png)

#### Add Task
- By selecting option 1 from the view and manage tasks menu, the user is guided through the process of adding a task.
- The user is prompted to enter a task description, category and priority.
- Throughout the app, if the user attempts to enter an empty description or description that exceeds the maximum character limit, they are presented with an error message and prompted to try again. This was implemented to ensure the user enters a valid task description.
- To ensure a smooth user experience, the user is prompted to enter a category (home, studies, work, exercise, hobbies) and priority (low, medium, high) based on a list of options. This was implemented to speed up the process of adding a task and to ensure the table / list of tasks is consistent and easy to read.

    ![Add Task](README-media/add-new-task.png)
- Once the user has entered a task description, category and priority, they are presented with the task details entered and prompted to confirm the addition of the task.

    ![Confirm New Task](README-media/confirm-new-task.png)
- If the user confirms the addition of the task, they are presented with a success message, the task is added to the spreadsheet and the user is returned to the view and manage tasks menu.
- The task ID / number is automatically generated and assigned to the task based on the number of tasks in the spreadsheet. This was implemented to ensure the task ID / number is unique and to ensure the user does not have to enter a task ID / number when adding a task.
- If the user does not confirm the addition of the task, they are presented with a message confirming the task was not added and are given the option to re-enter the task details. If the user chooses to re-enter the task details, they are returned to the add task prompt, but if they choose not to re-enter the task details, they are returned to the view and manage tasks menu.

#### Edit Task
- By selecting option 2 from the view and manage tasks menu, the user is guided through the process of editing a task.
- The table / list of tasks remains visible to the user while they are editing a task to ensure they can easily identify the task they wish to edit.
- The user is prompted to enter the task ID / number of the task they wish to edit.

    ![Edit Task ID Prompt](README-media/edit-task-id-prompt.png)
- If the user enters an invalid task ID / number, they are presented with an error message and prompted to try again.
- If the user selects a valid task ID / number, they are presented with the task details and prompted to confirm which field they wish to edit.

    ![Edit Task Field Prompt](README-media/edit-task-fields-prompt.png)
- After the user has selected the field they wish to edit, they are prompted to enter the new value for the field.
- Confirmation of the updated task details is presented to the user and they are prompted to confirm the update.

    ![Confirm Edit Task](README-media/confirm-edit-task.png)
- If the user confirms the updated task details, they are presented with a success message, the task is edited in the spreadsheet and the user is returned to the view and manage tasks menu.
- If the user does not confirm the updated task details, they are presented with a message confirming the changes were not saved and are given the option to re-enter the task details. If the user chooses to re-enter the task details, they are returned to the edit task prompt, but if they choose not to re-enter the task details, they are returned to the view and manage tasks menu.

#### Mark Task as Complete
- By selecting option 3 from the view and manage tasks menu, the user is guided through the process of marking a task as complete.
- The table / list of tasks remains visible to the user while they are marking a task as complete to ensure they can easily identify the task they wish to mark as complete.
- The user is prompted to enter the task ID / number of the task they wish to mark as complete.

    ![Mark Task as Complete Prompt](README-media/mark-task-as-complete-prompt.png)
- If the user enters an invalid task ID / number, they are presented with an error message and prompted to try again.
    
    ![Complete Task Invalid ID Prompt](README-media/complete-task-invalid-task-id.png)
- If the user selects a valid task ID / number, they are presented with the task details and prompted to confirm marking the task as complete.

    ![Confirm Complete Task Prompt](README-media/confirm-complete-task.png)
- If the user confirms marking the task as complete, they are presented with a success message, the task is marked as complete in the spreadsheet and the user is presented with an option to return to the view and manage tasks menu or exit the application.
- If the user does not confirm marking the task as complete, they are presented with a message confirming the task was not marked as complete and the user is returned to the view and manage tasks menu.

#### Remove Task
- By selecting option 4 from the view and manage tasks menu, the user is guided through the process of removing a task.
- The table / list of tasks remains visible to the user while they are removing a task to ensure they can easily identify the task they wish to remove.
- The user is prompted to enter the task ID / number of the task they wish to remove.

    ![Remove Task Prompt](README-media/remove-task-prompt.png)
- If the user enters an invalid task ID / number, they are presented with an error message and prompted to try again.

    ![Remove Task Invalid ID Prompt](README-media/remove-task-invalid-task-id.png)
- If the user selects a valid task ID / number, they are presented with the task details and prompted to confirm removing the task.

    ![Confirm Remove Task](README-media/confirm-remove-task.png)
- If the user confirms removing the task, they are presented with a success message, the task is removed from the spreadsheet and the user is presented with an option to return to the view and manage tasks menu or exit the application.
- If the user does not confirm removing the task, they are presented with a message confirming the task was not removed and the user is returned to the view and manage tasks menu.

#### View Completed Tasks
- By selecting option 5 from the view and manage tasks menu, the user is presented with a table / list of their completed tasks.

    ![View Completed Tasks](README-media/view-completed-tasks.png)
- The user is given the option to return to the view and manage tasks menu or exit the application.
- If there are no completed tasks, the user is presented with a message confirming there are no completed tasks and is returned to the view and manage tasks menu.

#### About Section
- By selecting option 2 from the homepage, the user is presented with information about Tidy Tasks.
- This includes a description of Tidy Tasks and a list of features.
- The About section has bee kept minimal and contains a splash of color to draw the user's attention to the information.

    ![About Section](README-media/about-section.png)
- The user is given the option to return to the homepage or exit the application.

### Future Features to Implement
- **Add Options to Completed Tasks** - Add the option to edit and re-open completed tasks.
- **Search & Sort Tasks** - Add the option to search and sort tasks by task ID / number, task description, category and priority.
- **Task Pages** - Adjust the view and manage tasks menu to display a maximum amount of tasks per page and add the option to navigate between pages.
- **Refactor Code** - Refactor the code to make it more efficient and even easier to read.

## Testing
### Linter Testing
- This application was tested using [CI Python Linter](https://pep8ci.herokuapp.com/). No errors were found.

    ![Linter Testing](README-media/linter-testing.png)

### Manual Testing
#### Test 1: Homepage Navigation

| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1. | The user is taken to the view and manage tasks menu. | Pass |
| 3 | The user selects option 6 from the view and manage tasks menu. | The user is taken to the homepage. | Pass |
| 4 | The user selects option 2. | The user is taken to the about page. | Pass |
| 5 | The user presses enter on the about page. | The user is taken to the homepage. | Pass |
| 6 | The user selects option 3. | The user is presented with a confirmation message and the application is exited. | Pass |

#### Test 2: Homepage - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user inputs an invalid option. | The user is presented with an error message and prompted to try again. | Pass |

#### Test 3: View & Manage Tasks Menu
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 1 from the view and manage tasks menu. | The user is taken to the add task prompt. | Pass |
| 4 | The user selects option 2 from the view and manage tasks menu. | The user is taken to the edit task prompt. | Pass |
| 5 | The user selects option 3 from the view and manage tasks menu. | The user is taken to the mark task as complete prompt. | Pass |
| 6 | The user selects option 4 from the view and manage tasks menu. | The user is taken to the remove task prompt. | Pass |
| 7 | The user selects option 5 from the view and manage tasks menu. | The user is taken to the view completed tasks prompt. | Pass |
| 8 | The user selects option 6 from the view and manage tasks menu. | The user is taken to the homepage. | Pass |

#### Test 4: View & Manage Tasks Menu - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user inputs an invalid option. | The user is presented with an error message and prompted to try again. | Pass |

#### Test 5: Add Task
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 1 from the view and manage tasks menu. | The user is taken to the add task prompt. | Pass |
| 4 | The user is prompted to enter a task description. | The user enters a task description & is taken to the next step. | Pass |
| 5 | The user is prompted to enter a category. | The user enters a category & is taken to the next step. | Pass |
| 6 | The user is prompted to enter a priority. | The user enters a priority & is taken to the next step. | Pass |
| 7 | The user is presented with the task details entered and prompted to confirm the addition of the task. | The user confirms the addition of the task, is presented with a success message, the task is added to the spreadsheet and the user is returned to the view and manage tasks menu. | Pass |
| 8 | Instead of confirming the addition of the task, the user selects no. | The user is presented with a message confirming the task was not added and is given the option to re-enter the task details. | Pass |
| 9 | The user selects yes when prompted to re-enter the task details. | The user is returned to the add task prompt. | Pass |
| 10 | The user selects no when prompted to re-enter the task details. | The user is returned to the view and manage tasks menu. | Pass |

#### Test 6: Add Task - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 1 from the view and manage tasks menu. | The user is taken to the add task prompt. | Pass |
| 4 | The user attempts to add a task without entering a task description. | The user is presented with an error message and prompted to try again. | Pass |
| 5 | The user attempts to add a description that exceeds the maximum character limit. | The user is presented with an error message and prompted to try again. | Pass |
| 6 | The user enters a valid task description. | The user is prompted to enter a category. | Pass |
| 7 | The user attempts to add a task without entering a category. | The user is presented with an error message and prompted to try again. | Pass |
| 8 | The user attempts to add an invalid category. | The user is presented with an error message and prompted to try again. | Pass |
| 9 | The user enters a valid category. | The user is prompted to enter a priority. | Pass |
| 10 | The user attempts to add a task without entering a priority. | The user is presented with an error message and prompted to try again. | Pass |
| 11 | The user attempts to add an invalid priority. | The user is presented with an error message and prompted to try again. | Pass |
| 12 | The user enters a valid priority. | The user is presented with the task details entered and prompted to confirm the addition of the task. | Pass |
| 13 | The user attempts to confirm the addition of the task without selecting an option. | The user is presented with an error message and prompted to try again. | Pass |
| 14 | The user attempts to confirm the addition of the task by selecting an invalid option. | The user is presented with an error message and prompted to try again. | Pass |
| 15 | The user confirms the addition of the task. | The user is presented with a success message, the task is added to the spreadsheet and the user is returned to the view and manage tasks menu. | Pass |
| 16 | Instead of confirming the addition of the task, the user selects no. | The user is presented with a message confirming the task was not added and is given the option to re-enter the task details. | Pass |
| 17 | The user presses enter without selecting an option. | The user is presented with an error message and prompted to try again. | Pass |
| 18 | The user selects an invalid option. | The user is presented with an error message and prompted to try again. | Pass |
| 19 | The user selects yes when prompted to re-enter the task details. | The user is returned to the add task prompt. | Pass |
| 20 | The user selects no when prompted to re-enter the task details. | The user is returned to the view and manage tasks menu. | Pass |

#### Test 7: Edit Task
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 2 from the view and manage tasks menu. | The user is taken to the edit task prompt. | Pass |
| 4 | The user is prompted to enter a task ID / number. | The user enters a task ID / number & is taken to the next step. | Pass |
| 5 | The user is presented with the task details and prompted to confirm which field they wish to edit. | The user selects an option & is taken to the next step. | Pass |
| 6 | The user is prompted to enter the new value for the field. | The user enters a new value & is taken to the next step. | Pass |
| 7 | The user is presented with the updated task details and prompted to confirm the update. | The user confirms the update, is presented with a success message, the task is edited in the spreadsheet and the user is presented with an option to return to the view and manage tasks menu or exit the application. | Pass |
| 8 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 9 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |
| 10 | Instead of confirming the update, the user selects no. | The user is presented with a message confirming the changes were not saved and is given the option to re-enter the task details. | Pass |
| 11 | The user selects yes when prompted to re-enter the task details. | The user is returned to the edit task prompt. | Pass |
| 12 | The user selects no when prompted to re-enter the task details. | The user is returned to the view and manage tasks menu. | Pass |

#### Test 8: Edit Task - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 2 from the view and manage tasks menu. | The user is taken to the edit task prompt. | Pass |
| 4 | The user attempts to edit a task without entering a task ID / number. | The user is presented with an error message and prompted to try again. | Pass |
| 5 | The user attempts to edit a task with an invalid task ID / number. | The user is presented with an error message and prompted to try again. | Pass |
| 6 | The user enters a valid task ID / number. | The user is presented with the task details and prompted to confirm which field they wish to edit. | Pass |
| 7 | The user attempts to confirm which field they wish to edit without selecting an option. | The user is presented with an error message and prompted to try again. | Pass |
| 8 | The user attempts to confirm which field they wish to edit by selecting an invalid option. | The user is presented with an error message and prompted to try again. | Pass |
| 9 | The user selects option 1. | The user is prompted to enter the new value for the description field. | Pass |
| 10 | The user attempts to confirm the update without entering a new value. | The user is presented with an error message and prompted to try again. | Pass |
| 11 | The user attempts to confirm the update with a new value that exceeds the maximum character limit. | The user is presented with an error message and prompted to try again. | Pass |
| 12 | The user enters a valid new value. | The user is presented with the updated task details and prompted to confirm the update. | Pass |
| 13 | The user attempts to confirm the update without selecting an option. | The user is presented with an error message and prompted to try again. | Pass |
| 14 | The user attempts to confirm the update by selecting an invalid option. | The user is presented with an error message and prompted to try again. | Pass |
| 15 | The user confirms the update. | The user is presented with a success message, the task is edited in the spreadsheet and the user is presented with an option to return to the view and manage tasks menu or exit the application. | Pass |
| 16 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 17 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |
| 18 | Instead of confirming the update, the user selects no. | The user is presented with a message confirming the changes were not saved and is given the option to re-enter the task details. | Pass |
| 19 | The user selects yes when prompted to re-enter the task details. | The user is returned to the edit task prompt. | Pass |
| 20 | The user selects no when prompted to re-enter the task details. | The user is returned to the view and manage tasks menu. | Pass |

#### Test 9: Mark Task as Complete
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 3 from the view and manage tasks menu. | The user is taken to the mark task as complete prompt. | Pass |
| 4 | The user is prompted to enter a task ID / number. | The user enters a task ID / number & is taken to the next step. | Pass |
| 5 | The user is presented with the task details, is prompted to confirm marking the task as complete and selects yes. | The user is presented with a success message, the task is marked as complete and the user is presented with an option to return to the view and manage tasks menu or exit the application. | Pass |
| 6 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 7 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |
| 8 | Instead of confirming marking the task as complete, the user selects no. | The user is presented with a message confirming the task was not marked as complete and the user is returned to the view and manage tasks menu. | Pass |

#### Test 10: Mark Task as Complete - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 3 from the view and manage tasks menu. | The user is taken to the mark task as complete prompt. | Pass |
| 4 | The user attempts to mark a task as complete without entering a task ID / number. | The user is presented with an error message and prompted to try again. | Pass |
| 5 | The user attempts to mark a task as complete with an invalid task ID / number. | The user is presented with an error message and prompted to try again. | Pass |
| 6 | The user enters a valid task ID / number. | The user is presented with the task details and is prompted to confirm marking the task as complete. | Pass |
| 7 | The user attempts to confirm marking the task as complete without selecting an option. | The user is presented with an error message and prompted to try again. | Pass |
| 8 | The user attempts to confirm marking the task as complete by selecting an invalid option. | The user is presented with an error message and prompted to try again. | Pass |
| 9 | The user confirms marking the task as complete. | The user is presented with a success message, the task is marked as complete and the user is presented with an option to return to the view and manage tasks menu or exit the application. | Pass |
| 10 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 11 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |
| 12 | Instead of confirming marking the task as complete, the user selects no. | The user is presented with a message confirming the task was not marked as complete and the user is returned to the view and manage tasks menu. | Pass |

#### Test 11: Remove Task
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 4 from the view and manage tasks menu. | The user is taken to the remove task prompt. | Pass |
| 4 | The user is prompted to enter a task ID / number and enters a valid task ID / number. | The user is presented with the task details, is prompted to confirm removing the task and selects yes. | Pass |
| 5 | The user selects yes. | The user is presented with a success message, the task is removed from the spreadsheet and the user is presented with an option to return to the view and manage tasks menu or exit the application. | Pass |
| 6 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 7 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |
| 8 | Instead of confirming removing the task, the user selects no. | The user is presented with a message confirming the task was not removed and the user is returned to the view and manage tasks menu. | Pass |

#### Test 12: Remove Task - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 4 from the view and manage tasks menu. | The user is taken to the remove task prompt. | Pass |
| 4 | The user attempts to remove a task without entering a task ID / number. | The user is presented with an error message and prompted to try again. | Pass |
| 5 | The user attempts to remove a task with an invalid task ID / number. | The user is presented with an error message and prompted to try again. | Pass |
| 6 | The user enters a valid task ID / number. | The user is presented with the task details and is prompted to confirm removing the task. | Pass |
| 7 | The user attempts to confirm removing the task without selecting an option. | The user is presented with an error message and prompted to try again. | Pass |
| 8 | The user attempts to confirm removing the task by selecting an invalid option. | The user is presented with an error message and prompted to try again. | Pass |
| 9 | The user confirms removing the task. | The user is presented with a success message, the task is removed from the spreadsheet and the user is presented with an option to return to the view and manage tasks menu or exit the application. | Pass |
| 10 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 11 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |
| 12 | Instead of confirming removing the task, the user selects no. | The user is presented with a message confirming the task was not removed and the user is returned to the view and manage tasks menu. | Pass |

#### Test 13: View Completed Tasks
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 5 from the view and manage tasks menu. | The user is taken to the view completed tasks prompt and is presented with a table / list of their completed tasks as well as an option to return to the view and manage tasks menu or exit the application. | Pass |
| 4 | The user presses enter. | The user is returned to the view and manage tasks menu. | Pass |
| 5 | The user presses q. | The user is presented with a confirmation message and the application is exited. | Pass |

#### Test 14: View Completed Tasks - Error Handling
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application. | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 1 from the homepage. | The user is presented with a table / list of their open tasks and a menu of options to manage their tasks. | Pass |
| 3 | The user selects option 5 from the view and manage tasks menu, but there are no completed tasks. | The user is presented with a message confirming there are no completed tasks and is returned to the view and manage tasks menu. | Pass |

#### Test 15: About
| Step | Action | Expected Outcome | Pass/Fail |
|------|--------|------------------|-----------|
| 1 | Open the application.  | The user is presented with the homepage & prompted to select an option from the menu. | Pass |
| 2 | The user selects option 2 from the homepage. | The user is taken to the about page. | Pass |
| 3 | The user presses enter. | The user is taken back to the homepage. | Pass |

### Bugs
#### Fixed Bugs
- The task ID calculation was not working as intended. The task ID was not being calculated based on the number of tasks in the spreadsheet, but was instead being calculated based on the number of rows in the spreadsheet. This was fixed by changing the calculation to count the number of tasks in the spreadsheet and then add 1 to the count to ensure the task ID is unique.
- An error would occur if there were no tasks in the spreadsheet. This was fixed by adding an if statement to check if there are any tasks in the spreadsheet and if there are no tasks, the user is presented with a message confirming there are no open tasks or no completed tasks.

#### Unfixed Bugs
- At certain points in the code, the clear screen function does not appear to work as intended. It partially clears the screen, but there is still some information from the previous slide left at the top of the screen. Throughout testing, this only appears to happen in Heroku, but not in the terminal / CMD.

## Deployment

### Heroku
The application is deployed on Heroku and can be accessed [here](https://tidy-tasks-9ed489f18853.herokuapp.com/).
To deploy the application on Heroku, follow the steps below:
1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in. For this project, the unique name is "tidy-tasks" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and locate the "Config Vars" section and click "Reveal config vars".
6. Add a config var:
   - In the "KEY" field enter "CREDS" in capital letters.
   - In the "VALUE" field copy and paste the contents of the creds.json file and click "Add".
7. Add another config var:
   - In the "KEY" field enter PORT in all capital letters.
   - In the "VALUE" field enter 8000 and click "Add".
8. Scroll to the "Buildpacks" section and click "Add buildpack".
9. Select Python and save changes.
10. Add another buildpack and select Nodejs then save changes again.
11. Ensure that the Python buildpack is above the Nodejs buildpack.
12. Navigate to the "Deploy" section by clicking the "Deploy" tab in the top navbar.
13. Select "GitHub" as the deployment method and click "Connect to GitHub".
14. Search for the GitHub repository name in the search bar.
15. Click on "connect" to link the repository to Heroku.
16. Scroll down and click on "Deploy Branch".
17. Once the app is deployed, Heroku will notify you and provide a button to view the app.

### Forking the GitHub Repository
This can be done to create a copy of the repository. The copy can be viewed and edited without affecting the original repository.

To fork the repository through GitHub, take the following steps:
1. In the "tidy-tasks" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository.

### Cloning the GitHub Repository
To clone the repository through GitHub:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Ensure HTTPS is selected in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### APIs
In order for the app to function as intended, APIs need to be set up and connected. In particular, the following APIs were used for this application:

- **Google Drive API** - This helps with getting credentials to access the files within Google drive.
- **Google Sheets API** - This is the API for the Google sheets where the data is stored for the app.

I followed the steps in a [video](https://www.youtube.com/watch?v=WTll5p4N7hE) from the Code Institute's Love Sandwiches project on how to set up and connect APIs.

## Credits
- Flowchart / diagram created using [Lucid Charts](https://www.lucidchart.com/pages/)
- Ascii Art created using [Patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
- The Code Institute community. In particular, the following members:
  - [Tony118g](https://github.com/Tony118g/doctor-diary)
  - [TerraBite147](https://github.com/TerraBite147)

## Technologies Used
- **Python:** The primary programming language used to create the application logic.
- **Google Sheets API:** For storing and retrieving task data from a spreadsheet, serving as a database.
- **Colorama:** To enhance the CLI experience with colored text for better readability.
- **GSpread:** A Python API for Google Sheets used for operations on the spreadsheet.