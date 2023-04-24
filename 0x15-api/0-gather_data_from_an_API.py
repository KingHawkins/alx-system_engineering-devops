#!/usr/bin/python3
"""
This script retrieves information from a REST API to display a report on tasks completed by an employee.

Inputs:
- employee_id: integer representing the ID of the employee to retrieve tasks for

Outputs:
- Prints a report showing the name of the employee, the number of tasks completed out of the total tasks, and a list of the completed tasks.

API:
This script uses the following REST API:
- https://jsonplaceholder.typicode.com/users/{employee_id}: retrieves information about the employee with the given ID.
- https://jsonplaceholder.typicode.com/todos/: retrieves a list of all tasks.

Usage: 
python3 employee_tasks.py employee_id

Example:
python3 employee_tasks.py 1
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    format_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    format_todo = "https://jsonplaceholder.typicode.com/todos/"
    response_user = requests.get(format_user).json()
    response_todo = requests.get(format_todo).json()
    name = response_user.get('name')
    (all_tasks, completed, storage) = 0, 0, []
    for item in response_todo:
        if item.get('userId') == int(argv[1]):
            all_tasks += 1
            if item.get('completed'):
                completed += 1
                storage.append("\t " + item.get('title'))
    print(f"Employee {name} is done with tasks({completed}/{all_tasks}):")
    print('\n'.join(item for item in storage))
