#!/usr/bin/python3
"""
prints the json format of the data.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    format_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    format_todo = "https://jsonplaceholder.typicode.com/todos/"
    response_user = requests.get(format_user).json()
    response_todo = requests.get(format_todo).json()
    (name, usrname) = response_user.get('name'), response_user.get('username')
    (all_tasks, completed, storage, status) = 0, 0, [], {}
    temp = []
    for item in response_todo:
        if item.get('userId') == int(argv[1]):
            jsfmt = {}
            all_tasks += 1
            jsfmt['task'] = item.get('title')
            jsfmt['completed'] = item.get('completed')
            jsfmt['username'] = usrname
            temp.append(jsfmt)
            status[item.get('title')] = item.get('completed')
            if item.get('completed'):
                completed += 1
                storage.append("\t " + item.get('title'))
    with open(f"{argv[1]}.json", "w") as out:
        dump, dump[argv[1]] = {}, temp
        json.dump(dump, out)
