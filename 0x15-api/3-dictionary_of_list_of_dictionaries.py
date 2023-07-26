#!/usr/bin/python3
"""
Exporting all employee information in JSON format.
"""

import json
import requests


def get_user_tasks(user_id, url):
    todo_response = requests.get(url + "todos",
                                 params={"userId": user_id}).json()
    tasks = [
        {
            "task": todo.get("title"),
            "completed": todo.get("completed")
        }
        for todo in todo_response
    ]
    return tasks


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_users_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = get_user_tasks(user_id, url)
        all_users_tasks[user_id] = {
            "username": username,
            "tasks": tasks
        }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_users_tasks, jsonfile, indent=2)
