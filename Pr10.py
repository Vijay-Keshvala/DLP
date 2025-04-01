import re
import operator

def evaluate_expression(expression):
    try:
        # Define operator precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }
        
        def apply_operation(operators, values):
            op = operators.pop()
            right = values.pop()
            left = values.pop()
            values.append(operations[op](left, right))
        
        def greater_precedence(op1, op2):
            return precedence[op1] > precedence[op2]
        
        tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/^()]', expression)
        values = []
        operators = []
        
        for token in tokens:
            if token.isdigit() or re.match(r'\d+\.\d+', token):
                values.append(float(token))
            elif token in precedence:
                while (operators and operators[-1] != '(' and
                       greater_precedence(operators[-1], token)):
                    apply_operation(operators, values)
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operation(operators, values)
                operators.pop()
        
        while operators:
            apply_operation(operators, values)
        
        return values[0]
    except Exception:
        return "Invalid expression"

# Sample test cases
expressions = [
    "(3 + 5) * 2 ^ 3",
    "3 + 5 * 2",
    "3 + 5 * 2 ^ 2",
    "3 + (5 * 2)",
    "3 + 5 ^ 2 * 2",
    "3 * (5 + 2)",
    "(3 + 5) ^ 2",
    "3 ^ 2 * 3",
    "3 ^ 2 + 5 * 2",
    "(3 + 5 * 2 ^ 2 - 8) / 4 ^ 2 + 6"
]

for expr in expressions:
    print(f"Expression: {expr} -> Result: {evaluate_expression(expr)}")
