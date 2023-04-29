#!/usr/bin/python3
"""
Prints employee number.
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
