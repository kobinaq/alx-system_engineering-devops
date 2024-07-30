#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports to CSV."""
import csv
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

        csv_filename = f"{employee_id}.csv"
        csv_data = []
        for todo in todos:
            csv_data.append([
                str(employee_id),
                user.get('username'),
                str(todo.get('completed')),
                todo.get('title')
            ])

        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerows(csv_data)

        print(f"Data exported to {csv_filename}")

    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Unexpected data structure in API response. Missing key: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Unable to write to file. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
