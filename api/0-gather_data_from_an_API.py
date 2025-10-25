#!/usr/bin/python3
"""
Module to fetch and display employee TODO list progress from REST API.

This script retrieves employee information and their TODO list from
JSONPlaceholder API and displays the completion progress.
"""
import requests
import sys


if __name__ == "__main__":
        if len(sys.argv) < 2:
                    print("Usage: {} <employee_id>".format(sys.argv[0]))
                            sys.exit(1)

                                try:
                                            employee_id = int(sys.argv[1])
                                                except ValueError:
                                                            print("Error: Employee ID must be an integer")
                                                                    sys.exit(1)

                                                                        # Base URL for the API
                                                                            base_url = "https://jsonplaceholder.typicode.com"

                                                                                # Fetch employee information
                                                                                    user_url = "{}/users/{}".format(base_url, employee_id)
                                                                                        user_response = requests.get(user_url)

                                                                                            if user_response.status_code != 200:
                                                                                                        print("Error: Unable to fetch employee data")
                                                                                                                sys.exit(1)

                                                                                                                    user_data = user_response.json()
                                                                                                                        employee_name = user_data.get("name")

                                                                                                                            # Fetch TODO list for the employee
                                                                                                                                todos_url = "{}/todos?userId={}".format(base_url, employee_id)
                                                                                                                                    todos_response = requests.get(todos_url)

                                                                                                                                        if todos_response.status_code != 200:
                                                                                                                                                    print("Error: Unable to fetch TODO list")
                                                                                                                                                            sys.exit(1)

                                                                                                                                                                todos_data = todos_response.json()

                                                                                                                                                                    # Calculate statistics
                                                                                                                                                                        total_tasks = len(todos_data)
                                                                                                                                                                            completed_tasks = [task for task in todos_data if task.get("completed")]
                                                                                                                                                                                number_of_done_tasks = len(completed_tasks)

                                                                                                                                                                                    # Display the results
                                                                                                                                                                                        print("Employee {} is done with tasks({}/{}):".format(
                                                                                                                                                                                                    employee_name, number_of_done_tasks, total_tasks))

                                                                                                                                                                                            # Display completed task titles
                                                                                                                                                                                                for task in completed_tasks:
                                                                                                                                                                                                            print("\t {}".format(task.get("title")))
