import re

def generate_quadruples(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    temp_counter = 1
    output = []
    
    def apply_operation(operators, operands):
        nonlocal temp_counter
        op = operators.pop()
        right = operands.pop()
        left = operands.pop()
        temp_var = f"t{temp_counter}"
        temp_counter += 1
        output.append((op, left, right, temp_var))
        operands.append(temp_var)
    
    tokens = re.findall(r'\d+|[+\-*/()]', expression)
    operands = []
    operators = []
    
    for token in tokens:
        if token.isdigit():
            operands.append(token)
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                apply_operation(operators, operands)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operation(operators, operands)
            operators.pop()
    
    while operators:
        apply_operation(operators, operands)
    
    return output

# Sample expression
expression = "9 + 42 * 8"
quadruples = generate_quadruples(expression)

# Printing the quadruples table
print("\nQuadruple Representation:")
print("{:<10} {:<10} {:<10} {:<10}".format("Operator", "Operand1", "Operand2", "Result"))
for quad in quadruples:
    print("{:<10} {:<10} {:<10} {:<10}".format(quad[0], quad[1], quad[2], quad[3]))
