#!/usr/bin/python3

"""
Module to retrieve and display employee TODO list progress.
"""

import requests
import sys


def retrieve_todo_list(employee_id):
    """
    Retrieve TODO list of a given employee and display progress.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        print(f"Employee {employee_name} is done with "
              f"tasks ({completed_tasks}/{total_tasks}):")

        for todo in todos_data:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    retrieve_todo_list(employee_id)
