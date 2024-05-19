#!/usr/bin/python3

# Simple To-Do List Manager (Task Manager)
# Task = description:, due_date:, completed: true/false
# TODO: Save to file or database

'''
A basic To-Do list application.
User should be able to add a task, mark task as completed
And remove a task from the list

## GUIDELINES
Use menu to interact with the application
Use functions to modularise code
Use data structures to manage tasks efficiently
Load tasks when the application starts
Save task when the application exits for a persistent task list
Handle errors correctly in cases where invalid input is made.

Menu items include:
- Add Task: Add a new task
- List Tasks: List/Load tasks
- Remove Task: Delete or remove a task
- Exit: Save and exit the application

## FEATURES
1. Add Tasks
2. List Tasks
3. Mark Task as Completed
4. Save & Load Tasks

## MODULES
- Display Menu
- Add Tasks
- List Tasks
- Mark Task as completed
- Save Tasks (Load Tasks)

## PSEUDOCODE
'''

# Menu
def help_menu():
    print("To-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Add Task
def add_task(description, due_date):
        task = {"description": description, "due_date": due_date, 'completion': False}
        tasks.append(task)

# Task Lists
def list_tasks():
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task['description']} (Due: {task['due_date']})")

# Remove a task
def remove_task(task_index):
    pass

# Mark as Completed
def mark_as_complete(task_index):
    pass

# Save/Load task
def save_tasks():
    pass

tasks = []
while True:
    help_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Task description: ")
        due_date = input("Due date: ")
        add_task(descriptin, due_date)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        remove_task(index)
    elif choice == '4':
        mark_as_complete(index)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
