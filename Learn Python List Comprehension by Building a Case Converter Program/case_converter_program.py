
# First approach - textbook code
# def convert_to_snake_case(pascal_or_camel_cased_string):
#   # Prepare a variable wherein we store here the characters
#   snake_cased_char_list = []

#   # Loop through the parameter
#   for char in pascal_or_camel_cased_string:
#     # Check if character is in uppercase
#     if char.isupper():
#       # If uppercase appeared, then that is the mark of a new word, we then add the underscore in front of it and append it to the list
#       converted_character = '_' + char.lower()
#       snake_cased_char_list.append(converted_character)
#     else:
#       # else, just append directly to the list
#       snake_cased_char_list.append(char)
      
#   # Use join to convert a list to a string
#   snake_cased_string = ''.join(snake_cased_char_list)
  
#   # If PascalCase, we should strip down the underscore in the beginning of the first word
#   clean_snake_cased_string = snake_cased_string.strip('_')

#   return clean_snake_cased_string


# Second approach - using list comprehension
def convert_to_snake_case(pascal_or_camel_cased_string):
  
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')
  
def main():
  print(convert_to_snake_case('AVeryVeryComplexString'))
  
# Call the function
main()