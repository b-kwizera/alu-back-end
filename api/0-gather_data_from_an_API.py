#!/usr/bin/python3
"""Module to fetch and display employee TODO list progress from REST API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get("{}/todos".format(base_url),
                                  params={"userId": employee_id})
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
