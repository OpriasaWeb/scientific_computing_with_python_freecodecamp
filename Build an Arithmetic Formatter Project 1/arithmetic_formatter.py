def arithmetic_arranger(problems, show_answers=False):
    # Rule 1: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        # Rule 2: Operator validation
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Rule 3: Numbers must only contain digits
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        # Rule 4: Each operand max 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width (longest number + 2 for operator + space)
        width = max(len(first), len(second)) + 2

        # Format each part
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dashes_line.append("-" * width)

        if show_answers == True:
            result = str(int(first) + int(second)) if operator == '+' else str(int(first) - int(second))
            answers_line.append(result.rjust(width))

    # Build arranged string
    problems = "    ".join(first_line) + "\n" \
             + "    ".join(second_line) + "\n" \
             + "    ".join(dashes_line)

    if show_answers == True:
        problems += "\n" + "    ".join(answers_line)

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')