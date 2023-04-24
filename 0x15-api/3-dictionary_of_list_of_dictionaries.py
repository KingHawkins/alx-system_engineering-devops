#!/usr/bin/python3
"""
prints the json format of the all data in the api.
"""
import json
import os
import requests
from sys import argv


if __name__ == '__main__':
    for i in range(1, 10):
        format_user = f"https://jsonplaceholder.typicode.com/users/{i}"
        format_todo = "https://jsonplaceholder.typicode.com/todos/"
        response_user = requests.get(format_user).json()
        response_todo = requests.get(format_todo).json()
        (name, unm) = response_user.get('name'), response_user.get('username')
        (all_tasks, completed, storage, status) = 0, 0, [], {}
        temp = []
        for item in response_todo:
            if item.get('userId') == i:
                jsfmt = {}
                all_tasks += 1
                jsfmt['task'] = item.get('title')
                jsfmt['completed'] = item.get('completed')
                jsfmt['username'] = unm
                temp.append(jsfmt)
                status[item.get('title')] = item.get('completed')
                if item.get('completed'):
                    completed += 1
                    storage.append("\t " + item.get('title'))
        if os.path.exists("todo_all_employees.json"):
            with open('todo_all_employees.json', 'r') as f:
                data = json.load(f)
                data[i] = temp

            with open('todo_all_employees.json', 'w') as f:
                json.dump(data, f)

        else:
            with open("todo_all_employees.json", "w") as out:
                dump, dump[i] = {}, temp
                json.dump(dump, out)
