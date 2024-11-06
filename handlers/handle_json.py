import json
import os


# Ensure data.json is initialized with an empty JSON object if missing or empty
def initialize_data_file():
    if not os.path.exists('data.json') or os.path.getsize('data.json') == 0:
        with open('data.json', 'w') as file:
            json.dump({}, file)  # Write an empty JSON object


# Load specific data from "data.json"
def read_data(key):
    initialize_data_file()  # Ensure data.json is initialized

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data.get(key)
    except json.JSONDecodeError:
        print("Warning: 'data.json' contains invalid JSON.")
        return None


# Write specific data to "data.json"
def write_data(key, value):
    initialize_data_file()  # Ensure data.json is initialized

    # Load existing data
    with open('data.json', 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}  # Start fresh if JSON is invalid

    # Update data with new key-value pair
    data[key] = value

    # Write updated data back to data.json
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    return value
