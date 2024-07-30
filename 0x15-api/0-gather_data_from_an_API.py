#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
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
        user_response = requests.get(f"{url}users/{employee_id}")
        user_response.raise_for_status()
        user = user_response.json()

        todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
        todos_response.raise_for_status()
        todos = todos_response.json()

        completed = [t.get("title") for t in todos if t.get("completed") is True]

        print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")
        [print(f"\t {c}") for c in completed]

    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Unexpected data structure in API response. Missing key: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
