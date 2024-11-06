import random
import string

# Define character sets
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation


def generate_password(length, use_upper, use_lower, use_digits, use_special_characters):
    # Initialize the password list and character pool
    generated_passwords = []
    character_pool = ""

    # Ensure at least one character from each selected category
    if use_upper:
        generated_passwords.append(random.choice(uppercase_letters))
        character_pool += uppercase_letters
    if use_lower:
        generated_passwords.append(random.choice(lowercase_letters))
        character_pool += lowercase_letters
    if use_digits:
        generated_passwords.append(random.choice(digits))
        character_pool += digits
    if use_special_characters:
        generated_passwords.append(random.choice(special_characters))
        character_pool += special_characters

    # Check if the character pool is empty
    if not character_pool:
        raise Exception("Character pool is empty! At least one character type must be selected.")

    # generated_passwords.clear() -> removed since it was clearing the character_list
    # list after being cleared was being populated with completely random characters irrespective of user preference

    # If the password is shorter than the desired length, fill the rest from the pool
    while len(generated_passwords) < length:
        generated_passwords.append(random.choice(character_pool))

    # Shuffle the password to ensure randomness in character placement
    random.shuffle(generated_passwords)

    return ''.join(generated_passwords)
