#!/usr/bin/python3
"""
Python script that, uses a REST API,
for a given employee ID, returns information about his/her TODO list progress
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    format_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    format_todo = "https://jsonplaceholder.typicode.com/todos/"
    response_user = requests.get(format_user).json()
    response_todo = requests.get(format_todo).json()
    (name, usrname) = response_user.get('name'), response_user.get('username')
    (all_tasks, completed, storage, status) = 0, 0, [], {}
    for item in response_todo:
        if item.get('userId') == int(argv[1]):
            all_tasks += 1
            status[item.get('title')] = item.get('completed')
            if item.get('completed'):
                completed += 1
                storage.append("\t " + item.get('title'))
    with open(f"{argv[1]}.csv", "w", newline="") as cs:
        writer = csv.writer(cs)
        #writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
         #                "TASK_TITLE"])
        for task, complete in status.items():
            writer.writerow([f'{argv[1]}', f"{usrname}", f"{complete}",
                             f"{task}"])
