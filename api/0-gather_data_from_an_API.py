#!/usr/bin/python3
"""Module to fetch and display employee TODO list progress from REST API.

This script retrieves employee information and their TODO list from
JSONPlaceholder API and displays the completion progress.
"""
import requests
import sys


if __name__ == "__main__":
        if len(sys.argv) != 2:
                    sys.exit(1)

                        employee_id = sys.argv[1]
                            user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
                                todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

                                    # Fetch data
                                        user = requests.get(user_url).json()
                                            todos = requests.get(todos_url).json()

                                                employee_name = user.get("name")
                                                    total_tasks = len(todos)
                                                        done_tasks = [task for task in todos if task.get("completed")]

                                                            print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
                                                                for task in done_tasks:
                                                                            print(f"\t {task.get('title')}")

