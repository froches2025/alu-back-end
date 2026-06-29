#!/usr/bin/python3

import requests
import sys


def fetch_todo_progress(employee_id: int):

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info_url = f'{base_url}users/{employee_id}'
    todo_info_url = f'{base_url}todos?userId={employee_id}'

    user_response = requests.get(user_info_url)
    user_info = user_response.json()
    user_name = user_info.get('name')

    todo_info = requests.get(todo_info_url)
    todo_response = todo_info.json()
    total_todos = len(todo_response)
    completed_todos = sum(todo.get("completed", False) for todo in todo_response)

    print(f"Employee {user_name} is done with tasks({completed_todos}/{total_todos}):")
    
    for todo in todo_response:
        if todo.get('completed', False):
            print(f"{todo.get('title')}")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Call the function to get and display TODO list progress
    fetch_todo_progress(employee_id)