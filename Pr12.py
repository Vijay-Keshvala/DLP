import re
import sympy as sp

def optimize_expression(expression):
    tokens = re.findall(r'\d+|[a-zA-Z]+|[+\-*/()]', expression)
    new_expr = []
    temp_stack = []
    
    for token in tokens:
        if token.isdigit():
            temp_stack.append(token)
        elif token in '+-*/':
            while len(temp_stack) >= 2 and temp_stack[-1].isdigit() and temp_stack[-2].isdigit():
                b = temp_stack.pop()
                a = temp_stack.pop()
                result = str(eval(a + token + b))
                temp_stack.append(result)
            temp_stack.append(token)
        else:
            while len(temp_stack) >= 3 and temp_stack[-2] in '+-*/' and temp_stack[-1].isdigit() and temp_stack[-3].isdigit():
                b = temp_stack.pop()
                op = temp_stack.pop()
                a = temp_stack.pop()
                result = str(eval(a + op + b))
                temp_stack.append(result)
            temp_stack.append(token)
    
    new_expr = ''.join(temp_stack)
    return new_expr

def generate_quadruples(expression):
    tokens = re.findall(r'\d+|[a-zA-Z]+|[+\-*/()]', expression)
    stack = []
    temp_counter = 1
    quadruples = []
    
    for token in tokens:
        if token.isdigit() or token.isalpha():
            stack.append(token)
        elif token in '+-*/':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                temp_var = f't{temp_counter}'
                quadruples.append((token, a, b, temp_var))
                stack.append(temp_var)
                temp_counter += 1
    
    return quadruples

def display_quadruples(quadruples):
    print("\nQuadruple Representation:")
    print("Operator | Operand 1 | Operand 2 | Result")
    print("---------------------------------------")
    for op, op1, op2, res in quadruples:
        print(f"{op:^8} | {op1:^9} | {op2:^9} | {res}")

if __name__ == "__main__":
    input_expression = "5 + x - 3 * 2"
    print("Original Expression:", input_expression)
    optimized_expression = optimize_expression(input_expression)
    print("Optimized Expression:", optimized_expression)
    quadruples = generate_quadruples(optimized_expression)
    display_quadruples(quadruples)
