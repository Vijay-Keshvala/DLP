import pandas as pd
from collections import defaultdict

def construct_parsing_table(grammar, first_sets, follow_sets):
    parsing_table = defaultdict(dict)
    is_ll1 = True
    
    for non_terminal, productions in grammar.items():
        for production in productions:
            first_set = get_first_of_production(production, first_sets)
            
            for terminal in first_set:
                if terminal != 'ε':
                    if terminal in parsing_table[non_terminal]:
                        is_ll1 = False
                    parsing_table[non_terminal][terminal] = production
            
            if 'ε' in first_set:
                for terminal in follow_sets[non_terminal]:
                    if terminal in parsing_table[non_terminal]:
                        is_ll1 = False
                    parsing_table[non_terminal][terminal] = 'ε'
    
    return parsing_table, is_ll1

def get_first_of_production(production, first_sets):
    first = set()
    for symbol in production:
        if symbol in first_sets:
            first |= first_sets[symbol] - {'ε'}
            if 'ε' not in first_sets[symbol]:
                break
        else:
            first.add(symbol)
            break
    else:
        first.add('ε')
    return first

def parse_string(parsing_table, start_symbol, input_string):
    stack = ["$"]
    stack.insert(0, start_symbol)
    input_string += "$"
    
    index = 0
    print("\nParsing Input String:", input_string[:-1])
    while stack:
        top = stack.pop(0)
        if top == input_string[index]:
            index += 1
        elif top in parsing_table and input_string[index] in parsing_table[top]:
            production = parsing_table[top][input_string[index]]
            if production != "ε":
                stack[:0] = list(production)
        else:
            return "Invalid string"
    return "Valid string" if index == len(input_string) else "Invalid string"

# Updated Grammar
grammar = {
    'S': ["abc", "ac", "(abc)", "c", "(ac)"],
    'A': ["a", "()", "(ab)", "abcabc", "b"]
}

first_sets = {
    'S': {'a', '(', 'c'},
    'A': {'a', '(', 'b'}
}

follow_sets = {
    'S': {'$', ')'},
    'A': {'$', ')'}
}

parsing_table, is_ll1 = construct_parsing_table(grammar, first_sets, follow_sets)

df = pd.DataFrame(parsing_table).fillna("-")
df = df.T  # Transpose to align properly
print("Predictive Parsing Table:")
print(df.to_string())
print("\nGrammar is LL(1)" if is_ll1 else "\nGrammar is NOT LL(1)")

input_string = "ac"
print("\nValidation Result:", parse_string(parsing_table, 'S', input_string))
