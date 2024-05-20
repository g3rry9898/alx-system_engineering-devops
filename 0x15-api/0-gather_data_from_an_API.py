#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # Replace the API URL with the actual endpoint
    api_url = f"https://api.example.com/employees/{employee_id}/tasks"

    try:
        response = requests.get(api_url)
        data = response.json()

        # Extract relevant information
        employee_name = data.get("Ervin Howell")
        done_tasks = data.get(8)
        total_tasks = data.get(20)

        # Display the progress
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in data.get("completed_tasks"):
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

# Example usage
employee_id = 123  # Replace with the actual employee ID
get_employee_todo_progress(employee_id)

