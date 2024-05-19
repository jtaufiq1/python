#!/usr/bin/python3

import os
#import argparse
#import datetime
import csv
#import sqlite3

'''
# TO-DO LIST
A simple To-Do List to manage tasks

## DESCRIPTION
Load task from a csv file or database upon start.
Task Description:Description, Due date and Completion status (true/false).

User should be able to add a task, mark task as completed
And remove a task from the list
The tasks list should be saved to file(csv) or a database(sqlite) before exiting.

## GUIDELINES
Use menu to interact with the application
Use functions to modularise code
Use data structures to manage tasks efficiently
Load tasks when the application starts
Save task when the application exits for a persistent task list
Handle errors correctly in cases where invalid input are made.

Menu items include:
- Add Task: Add a new task
- List Tasks: List/Load tasks
- Mark Task as Complete: Manually mark task as complete
- Remove Task: Delete or remove a task
- Exit: Save Tasks and exit the application

## FEATURES
1. Add Tasks
2. List Tasks
3. Mark Task as Completed
4. Remove Task
5. Save & Load Tasks

## MODULES
- Display Menu
- Add Tasks
- List Tasks
- Mark Task as completed
- Remove task
- Save Tasks (Load Tasks)

## TODO:
- Reformat Task Structure to
  title, due date, completion status & task description
- Get Task Index
- Task Length
- Date/Time format
- Load tasks
- Write Tasks to [csv,sqlite]
'''

# Menu
print("\t\tTo-Do List Manager".upper())
def help_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

# Add Task
def add_task(description, due_date):
    task = {'description':description,'due_date':due_date,'completed': 'false'}
    tasks.append(task)

# Task Lists
def list_tasks():
    status = ''
    for index, task in enumerate(tasks, 0):
        if task['completed'] == 'true':
            status = "✓"
        else:
            status = " "
        print(f"{index+1}. [{status}] {task['description']} [{task['due_date']}]")

# Remove a task
def remove_task():
    list_tasks()
    task_index = int(input("Remove Task: "))

    # task_index >= 0 && task_index < len(tasks):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]

# Mark Task as Completed
def mark_as_complete():
    list_tasks()
    task_index = int(input("Task Index: "))

    # task_index >= 0 && task_index < len(tasks):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = 'true'

# Save/Load task
def load_tasks():
    TODO_FILE = "todo.csv"
    if os.path.exists(TODO_FILE): # Load file
        with open(TODO_FILE, 'r') as file:
            todo_file = list(csv.reader(file))
            for td in todo_file:
                if '#;' in td[0]:
                    print("Skipped")
                else:
                    desc = td[0]
                    due_date = td[1]
                    completed = td[2]
                    task = {'description':desc,'due_date':due_date,'completed': completed}
                    tasks.append(task)
                    print(task)
    else:
        with open(TODO_FILE,'w') as file:
            tasks_heading = "#;description;due_date;complete\n"
            sample_task = "task description here,20-jan-2024,false"
            file.write(tasks_heading)
            file.write(sample_task)

tasks = []
load_tasks()
mark_as_complete()
list_tasks()

'''
while True:
    help_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Task description: ")
        due_date = input("Due date: ")
        add_task(description, due_date)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_as_complete()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
'''
