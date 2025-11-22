full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    # --- Validate name ---
    if not isinstance(character_name, str):
        return "The character name should be a string"

    if len(character_name) > 10:
        return "The character name is too long"

    if " " in character_name:
        return "The character name should not contain spaces"

    # --- Validate stats ---
    stats = [strength, intelligence, charisma]

    # All must be integers
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"

    # All must be >= 1
    if not all(s >= 1 for s in stats):
        return "All stats should be no less than 1"

    # All must be <= 4
    if not all(s <= 4 for s in stats):
        return "All stats should be no more than 4"

    # Sum must be exactly 7
    if sum(stats) != 7:
        return "The character should start with 7 points"

    # --- Build output ---
    def stat_line(label, value):
        return f"{label} " + (full_dot * value) + (empty_dot * (10 - value))

    return (
        f"{character_name}\n"
        f"{stat_line('STR', strength)}\n"
        f"{stat_line('INT', intelligence)}\n"
        f"{stat_line('CHA', charisma)}"
    )
    
create_character("Sulfurturero", 2, 2, 2)