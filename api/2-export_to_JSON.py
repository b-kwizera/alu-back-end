#!/usr/bin/python3
"""
Export employee TODO list to a JSON file using a REST API.
"""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{emp_id}"
    todos_url = f"{base_url}/{emp_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    emp_username = user.get("username")
    tasks_list = []

    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": emp_username
        })

    data = {str(emp_id): tasks_list}

    with open(f"{emp_id}.json", "w") as json_file:
        json.dump(data, json_file)
