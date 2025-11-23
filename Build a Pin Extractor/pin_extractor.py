def pin_extractor(poems):
    # This list will store the secret code for each poem
    secret_codes = []
    
    # Loop through each poem in the provided list
    for poem in poems:
        # Start with an empty secret code for this poem
        secret_code = ''
        
        # Split poem into lines using newline as separator
        lines = poem.split('\n')
        
        # Loop through each line with its index
        for line_index, line in enumerate(lines):
            # Split the current line into words
            words = line.split()
            
            # Check if the line has enough words for the current index
            # Example: line_index = 2 → check if a 3rd word exists
            if len(words) > line_index:
                # Add the length of that word to the code
                secret_code += str(len(words[line_index]))
            else:
                # If not enough words, append '0'
                secret_code += '0'
        
        # Store the secret code for this poem
        secret_codes.append(secret_code)
    
    # Return the list of all secret codes
    return secret_codes


# Sample poems
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Extract PIN codes from the poems
print(pin_extractor([poem, poem2, poem3]))
