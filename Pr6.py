class RecursiveDescentParser:
    def __init__(self, input_str):
        self.input = input_str.replace(" ", "")  # Remove spaces
        self.index = 0

    def match(self, char):
        """Check if the current character matches the expected char."""
        if self.index < len(self.input) and self.input[self.index] == char:
            self.index += 1
            return True
        return False

    def S(self):
        """S → ( L ) | a"""
        if self.match('a'):
            return True
        elif self.match('('):
            if self.L():
                if self.match(')'):
                    return True
        return False

    def L(self):
        """L → S L’"""
        if self.S():
            return self.L_prime()
        return False

    def L_prime(self):
        """L’ → , S L’ | ϵ (optional)"""
        if self.match(','):
            if self.S():
                return self.L_prime()  # Continue parsing L'
            return False
        return True  # ϵ (epsilon case)

    def is_valid(self):
        """Check if the whole input is parsed correctly."""
        return self.S() and self.index == len(self.input)

# Test Cases
test_cases = [
    "(a)",        # Valid
    "a",          # Valid
    "(a,a)",      # Valid
    "(a,(a,a),a)", # Valid
    "(a,a),(a,a)", # Invalid
    "a)",         # Invalid
    "(a a,a",     # Invalid
    "a a, (a,a),a" # Invalid
]

for test in test_cases:
    parser = RecursiveDescentParser(test)
    print(f"Input: {test} → {'Valid string' if parser.is_valid() else 'Invalid string'}")
