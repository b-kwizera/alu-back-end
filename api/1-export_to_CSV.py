#!/usr/bin/python3
"""This module exports employee TODO list to a CSV file using a REST API.
"""
import csv
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

                                                    # Write CSV file
                                                        filename = f"{employee_id}.csv"
                                                            with open(filename, mode="w", newline="") as csv_file:
                                                                        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                                                                                for task in todos:
                                                                                                writer.writerow([employee_id,
                                                                                                                                              username,
                                                                                                                                              task.get("completed"),
                                                                                                                                              task.get("title")])

