#!/usr/bin/python3
"""Export employee TODO list to a JSON file using a REST API.
"""
import json
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
                                            username = user.get("username")

                                                # Build JSON data
                                                    tasks_list = []
                                                        for task in todos:
                                                                tasks_list.append({
                                                                            "task": task.get("title"),
                                                                                        "completed": task.get("completed"),
                                                                                                    "username": username
                                                                                                            })

                                                                                                                data = {employee_id: tasks_list}

                                                                                                                    # Write JSON file
                                                                                                                        filename = f"{employee_id}.json"
                                                                                                                            with open(filename, "w") as json_file:
                                                                                                                                    json.dump(data, json_file)
