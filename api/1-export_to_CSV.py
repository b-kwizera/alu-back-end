#!/usr/bin/python3
"""
Export employee TODO list to a CSV file using a REST API.
"""
import csv
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

    with open(f"{emp_id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                emp_username,
                task.get("completed"),
                task.get("title")
            ])
