#!/usr/bin/python3
"""
Export employee TODO list to a CSV file using a REST API.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    file_content = []

    todo_data = requests.get(todos_url).json()

    employee_name = requests.get(users_url).json()["username"]

    for todo in todo_data:
        if user_id == todo["userId"]:
            file_content.append(
                [str(user_id), employee_name, todo["completed"],
                 todo["title"]])

    print(file_content)
    file_name = "{}.csv".format(user_id)
    with open(file_name, 'w', newline='') as csv_file:
        write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in file_content:
            for item in row:
                str(item)
            write.writerow(row)
