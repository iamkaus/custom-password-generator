import uuid

from handlers.handle_json import read_data


def generate_user_identifier(user_attributes):
    # Check for existing UUID
    existing_uuid = read_data("user_identifier")
    if existing_uuid:
        return existing_uuid
    else:
        # Generate new UUID if none exists
        new_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(user_attributes)))
        return new_uuid
