#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file using a REST API.
"""
import json
import requests


if __name__ == "__main__":
        # Fetch all users
            users = requests.get("https://jsonplaceholder.typicode.com/users").json()
                todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

                    # Build dictionary with USER_ID as key
                        data = {}
                            for user in users:
                                        user_id = str(user.get("id"))
                                                username = user.get("username")
                                                        data[user_id] = []

                                                            for task in todos:
                                                                        user_id = str(task.get("userId"))
                                                                                data[user_id].append({
                                                                                                "username": users[int(user_id) - 1].get("username"),
                                                                                                            "task": task.get("title"),
                                                                                                                        "completed": task.get("completed")
                                                                                                                                })

                                                                                    # Write to JSON file
                                                                                        with open("todo_all_employees.json", "w") as json_file:
                                                                                                    json.dump(data, json_file)
