def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        # make a list to store the numbers
        numbers = []

        # loop through the input params, starting from 1 and
        # break once meet the condition in range stop
        for i in range(1, n + 1):
            # append each iteration with the form of string in numbers list
            numbers.append(str(i))
        # join them all
        return " ".join(numbers)

# Call the function
number_pattern(4)