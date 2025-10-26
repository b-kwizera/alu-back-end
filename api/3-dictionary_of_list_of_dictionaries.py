#!/usr/bin/python3
"""
Export all employees' TODO lists to a JSON file using a REST API.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url).json()

    all_data = {}

    for user in users:
        emp_id = user.get("id")
        emp_username = user.get("username")
        todos_url = f"{base_url}/{emp_id}/todos"
        todos = requests.get(todos_url).json()

        tasks_list = []
        for task in todos:
            tasks_list.append({
                "username": emp_username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_data[str(emp_id)] = tasks_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
