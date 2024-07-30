#!/usr/bin/python3
"""Fetches to-do list information for all employees and exports it to a JSON file."""
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch all users
        users_response = requests.get(f"{url}users")
        users_response.raise_for_status()
        users = users_response.json()

        # Prepare the dictionary to store all tasks
        all_tasks = {}

        # Fetch tasks for each user
        for user in users:
            user_id = user.get("id")
            username = user.get("username")

            todos_response = requests.get(f"{url}todos", params={"userId": user_id})
            todos_response.raise_for_status()
            todos = todos_response.json()

            # Prepare list to store tasks of the current user
            user_tasks = []
            for task in todos:
                task_info = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_info)

            # Add the user's tasks to the all_tasks dictionary
            all_tasks[user_id] = user_tasks

        # Write the data to a JSON file
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_tasks, json_file)

        print("Data has been exported to todo_all_employees.json")

    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
    except KeyError as e:
        print(f"Error: Unexpected data structure in API response. Missing key: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

