#!/usr/bin/python3
"""
a pthon script that uses REST API to return todo list
of employees
"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_response = requests.get(
            base_url + 'users/{}'.format(employee_id)
            ).json()
    todo_response = requests.get(
            base_url + 'todos', params={'userId': employee_id}
            ).json()

    completed_tasks = [
            task['title'] for task in todo_response if task['completed']
            ]
    total_tasks = len(todo_response)

    print(f"Employee {user_response['name']} is done with tasks ", end="")
    print(f"({len(completed_tasks)}/{total_tasks}):")
    print("\n".join(f"\t{task}" for task in completed_tasks))
