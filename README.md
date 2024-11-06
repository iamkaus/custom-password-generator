# Password Generator

This is a simple Python-based password generator that creates secure, random passwords based on user-defined preferences
such as length, inclusion of uppercase letters, lowercase letters, digits, and special characters. The generated
passwords ensure a mix of selected character types and can be customized according to the user's needs.

## Features

- **Customizable Password Length**: Set the length of the password, from a minimum of 4 characters to a maximum of 15
  characters.
- **Character Type Selection**: Choose which character types to include in the password:
    - Uppercase Letters
    - Lowercase Letters
    - Digits
    - Special Characters (e.g., !, @, #, $, etc.)
- **Password Generation**: The generated password will contain at least one character from each selected category.
- **Multiple Passwords**: Generate multiple passwords at once with your chosen settings.
- **Session-Based User Tracking**: Each user session generates a unique UUID, ensuring personalized usage tracking
  without compromising privacy.

## Getting Started

Follow these instructions to clone the repository and run the project on your local machine.

### Prerequisites

- Python 3.x
- Git

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/iamkaus/password-generator.git

2. To run the password generator, execute the following command to navigate to the Project Directory:
     ```base
   cd password-generator

3. Run the Password Generator

   Execute the following command to start generating passwords:
      ```bash
   python main.py

4. The program will prompt you to specify your preferences (password length, character types, etc.), and it will
   generate the password based on your choices.
     ```bash
   Welcome to the Password Generator!
   Enter your username (required): ryo
   Enter your email (optional): 
   Do you want to customize your password? (yes/no): y
   Enter the desired password length (minimum 4): 15
   Include uppercase letters? (y/n): y
   Include lowercase letters? (y/n): y
   Include digits? (y/n): y
   Include special characters? (y/n): y
   How many passwords would you like to generate? 1
   
   # Following inputs showcased are nothing but for demonstration purposes

5. Output provided would be a mix of *Generated Passwords, Count Of Generated Passwords, User Uuid, and a List populated
   with Generated Passwords*.
    ```bash
   R46T{&jATF]_GW>
   Total Passwords Generated This Session: 1
   User UUID: 25d4552d-2e3d-5844-9b5b-29bf0dcc9dd2
   Generated Passwords: ['R46T{&jATF]_GW>']

6. Running_Unit_Tests

   Unit tests are provided to verify the correctness of the password generation logic. To run the tests, use:
    ```bash
   python -m unittest "test_working.py"
   # test_working.py is the testfile provided can be renamed as such and test cases can be changed/modified

### Additional Notes

- For users who are new to GitHub, you might also want to mention that they can download the project as a `.zip` file
  instead of cloning it with Git.

## Files and Directories

- **`Password Generator/`:** **Main/Root Directory**


- **`src/`**: Contains the source code of the project.
    - **`main.py`**: Entry point for running the password generator.
    - **`logic.py`**: Contains the main logic for password generation.
    - **`utils.py`**: Utility functions used by the password generator.
    - **`identifier.py`**: Generates and manages unique user session identifiers (UUIDs).


- **`handlers/`**: Contains the source code to handle `data.json` and `config.json`
    - **`handle_json.py`**: Handles reading and writing data to JSON files (e.g., user preferences, generated
      passwords).
    - **`handle_config.py`**: Handles reading and writing user configurations to JSON file (e.g., length, use_upper,
      use_lower, use_digit, use_special_characters)


- **`tests/`**: Contains the unit tests for the project.
    - **`test_working.py`:** Contains the default test cases (e.g., edge cases
      like `all characters TRUE and length == 15`)


- **`pkg_manager/`:** Contains `__init__.py`
    - **`__init__.py`**: Initializes the project environment and sets up functions.

## Contributing

**If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure
that your code follows the existing style and includes unit tests where applicable.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
