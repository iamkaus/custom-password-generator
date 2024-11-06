from handlers.handle_config import write_preferences, read_preferences


# get_user_preference() -> method determines if the user wants to set some flags of his own accord
# the flags are then returned as a tuple and unpacked at the call site


def get_user_preferences(customize):
    # -> logic to make sure an exception is thrown
    # -> if the user determined flag for password length falls below a certain length

    # assigning None to length variable to avoid conflicts like where
    """ if the input for the length is invalid and the loop continues,
    the length variable won't exist until it's assigned a valid value. """

    length = None

    # update_preference to check if user wants to update customisations or not
    update_preferences = customize

    if update_preferences:
        while True:
            try:
                length = int(input("Enter the desired password length (minimum 4): "))
                if length < 4 or length > 15:
                    print("Password length must be at least 4.")
                    continue  # Prompt the user again for a valid length
                break  # Break the loop if the length is valid
            except ValueError:
                print("Please enter a valid number.")
                continue  # Continue prompting if input is invalid

        # Other flags for password customization

        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special_characters = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Save updated preferences
        preferences = {
            "default_password_length": length,
            "use_upper": use_upper,
            "use_lower": use_lower,
            "use_digits": use_digits,
            "use_special_characters": use_special_characters
        }
        write_preferences(preferences)
        return length, use_upper, use_lower, use_digits, use_special_characters

    else:

        # preferences container to store preferences
        preferences = read_preferences()
        return tuple(preferences.values())  # return preference values as a tuple
