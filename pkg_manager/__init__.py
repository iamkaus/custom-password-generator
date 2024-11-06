# __init__.py

__version__ = "1.0.0"

from handlers.handle_json import read_data, write_data
from src.identifier import generate_user_identifier
from src.logic import generate_password
from src.utils import get_user_preferences

__all__ = [
    'generate_password',
    'get_user_preferences',
    'generate_user_identifier',
    'read_data',
    'write_data',
]


# Initialization logic
def initialize():
    print("Initializing Password Generator Package...")
    # You can add any other setup logic here if necessary
    # For example, loading configuration or checking dependencies


initialize()  # Call the initialization function
