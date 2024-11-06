from time import sleep

from handlers.handle_json import read_data, write_data
from identifier import generate_user_identifier
from logic import generate_password
from utils import get_user_preferences


def main():
    print("Welcome to the Password Generator!")

    # Initialize session counter and password list
    generated_password_counter = 0
    generated_passwords = []

    # user_attribute to gather/collect different user_attributes like user_name, email under one roof
    user_attributes = []

    # Loop until valid user attributes are collected
    while not user_attributes:
        username = input("Enter your username (required): ").strip()
        if username:  # Only add non-empty username
            user_attributes.append(username)
        else:
            print("Username cannot be empty. Please enter a valid username.")

        email = input("Enter your email (optional): ").strip()
        if email:  # Only add non-empty email
            user_attributes.append(email)

    # Check if the user wants to customize their password
    customize = input("Do you want to customize your password? (yes/no): ").strip().lower() == 'y'

    if customize:
        while True:
            # Get user preferences
            length, use_upper, use_lower, use_digits, use_special_characters = get_user_preferences(customize)

            while True:
                try:
                    num_passwords = int(input("How many passwords would you like to generate? "))

                    # Check if num_passwords is a valid positive integer
                    if num_passwords <= 0:
                        raise ValueError("Invalid input. Please enter a positive number.")
                    else:
                        break  # Valid input, exit loop
                except ValueError as e:
                    print(e)

            # Check if at least one of the flags is true
            try:
                # loop to iterate over the function to make sure num_password times passwords are generated
                for _ in range(num_passwords):
                    passwords = generate_password(length, use_upper, use_lower, use_digits, use_special_characters)
                    generated_passwords.append(passwords)
                    generated_password_counter += 1
                break
            except Exception as e:
                print(e)
                print("Please customize your password again.")

    # default case follows if customization is not opted for

    else:
        print("Stored password settings will apply. Please set your preferences to customize.")
        length, use_upper, use_lower, use_digits, use_special_characters = get_user_preferences(customize)

        # ask user for number of passwords to generate and to check for valid input by the user
        while True:
            try:
                num_passwords = int(input("How many passwords would you like to generate? "))

                # Check if num_passwords is a valid positive integer
                if num_passwords <= 0:
                    raise ValueError("Invalid input. Please enter a positive number.")
                else:
                    for _ in range(num_passwords):
                        password = generate_password(length, use_upper, use_lower, use_digits, use_special_characters)
                        generated_passwords.append(password)  # Store each password
                        generated_password_counter += 1  # Increment session counter
                    break  # Valid input, exit loop
            except ValueError as e:
                print(e)

    # Now write passwords after generation
    write_data("passwords", generated_passwords)

    # Display all generated passwords
    print("\nGenerated Passwords:")
    for pwd in generated_passwords:
        print(pwd)
        sleep(0.5)  # sleep to delay each iteration of loop by half a second.

    # Display the number of passwords generated in this session
    print("Total Passwords Generated This Session:", generated_password_counter)

    # Check if user UUID exists
    user_uuid = read_data("user_identifier")

    if not user_uuid:
        # Generate new UUID only if it doesn't exist
        user_uuid = generate_user_identifier(user_attributes)
        write_data("user_identifier", user_uuid)  # Write once here

    # Read and display stored data
    print("User UUID:", read_data("user_identifier"))
    print("Generated Passwords:", read_data("passwords"))


if __name__ == "__main__":
    main()
