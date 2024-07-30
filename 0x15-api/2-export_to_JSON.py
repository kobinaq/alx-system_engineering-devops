#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch user data
        user_response = requests.get(f"{url}users/{employee_id}")
        user_response.raise_for_status()
        user = user_response.json()
        username = user.get('username')

        # Fetch todos for the user
        todos_response = requests.get(f"{url}todos", 
                                      params={"userId": employee_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Prepare the data in the required format
        user_data = {
            str(employee_id): [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                }
                for todo in todos
            ]
        }

        # Write the data to a JSON file
        filename = f"{employee_id}.json"
        with open(filename, 'w') as jsonfile:
            json.dump(user_data, jsonfile)

        print(f"Data exported to {filename}")

    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Unexpected data structure in API response. "
              f"Missing key: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Unable to write to file. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
