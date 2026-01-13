def add_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"
    
    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = ["Current User Settings:"]
    for key, value in settings.items():
        result.append(f"{key.capitalize()}: {value}")
    
    return "\n".join(result) + "\n"


# Test dictionary
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}

if __name__ == "__main__":
    settings = {}

    # Add settings
    print(add_setting(settings, ("Theme", "Dark")))
    print(add_setting(settings, ("Language", "English")))

    # View settings once
    print("\n--- View Settings ---")
    print(view_settings(settings))  # ONLY ONE CALL

    # Update settings
    print(update_setting(settings, ("Theme", "Light")))
    print(update_setting(settings, ("Notifications", "Enabled")))  # non-existing

    # View settings again once
    print("\n--- View Settings After Update ---")
    print(view_settings(settings))  # ONLY ONE CALL

    # Delete settings
    print(delete_setting(settings, "Language"))
    print(delete_setting(settings, "Volume"))  # non-existing

    # Final view
    print("\n--- Final Settings ---")
    print(view_settings(settings))  # ONLY ONE CALL

