#!/usr/bin/python3
"""
Script that returns information about an employee's TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{emp_id}"
    todos_url = f"{base_url}/{emp_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    emp_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(
        f"Employee {emp_name} is done with their tasks"
        f"({len(done_tasks)}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")
