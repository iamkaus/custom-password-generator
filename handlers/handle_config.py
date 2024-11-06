import json
import os


# Ensure config.json is initialized with an empty JSON object if missing or empty
def initialize_data_file():
    if not os.path.exists('config.json') or os.path.getsize('config.json') == 0:
        with open('config.json', 'w') as file:
            json.dump({}, file)  # Write an empty JSON object


# Load user preferences from "config.json"
def read_preferences():
    if not os.path.exists('config.json') or os.path.getsize('config.json') == 0:
        # Return default preferences if config.json does not exist or is empty
        return {
            "default_password_length": 15,
            "use_upper": True,
            "use_lower": True,
            "use_digits": True,
            "use_special_characters": True
        }
    with open('config.json', 'r') as file:
        preferences = json.load(file)
        return preferences


# Write user preferences to "config.json"
def write_preferences(preferences):
    with open('config.json', 'w') as file:
        json.dump(preferences, file, indent=4)
