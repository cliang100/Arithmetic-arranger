def arithmetic_arranger(problems, show_answers=False):
    # For the purposes of this exercise, the equation limit is 5
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"line1": "", "line2": "", "line3": "", "line4": ""}
    for problem in problems:
        # Split problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operator is a + or -
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        # Error checks for operands
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Convert operands to integers for solution later
        num1 = int(operand1)
        num2 = int(operand2)

        # Find max length of an operand for dashes and spaces between equations
        max_length = max(len(operand1), len(operand2))

        # Arranging operands and operator into their respective equations
        arranged_problems["line1"] += operand1.rjust(max_length + 2) + '    '
        arranged_problems["line2"] += operator + ' ' + operand2.rjust(max_length) + '    '
        arranged_problems["line3"] += '-' * (max_length + 2) + '    '

        # Calculates equation if show_answers is True
        if show_answers:
            if operator == '+':
                solution = num1 + num2
                arranged_problems["line4"] += str(solution).rjust(max_length + 2) + '    '
            elif operator == '-':
                solution = num1 - num2
                arranged_problems["line4"] += str(solution).rjust(max_length + 2) + '    '

    final_arranged_problems = arranged_problems["line1"] + '\n' + arranged_problems["line2"] + '\n' + arranged_problems["line3"]
    if show_answers:
        final_arranged_problems += '\n' + arranged_problems["line4"]
    return final_arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"])) 