#include <stdio.h>
#include <ctype.h>
#include <string.h>

void lexicalAnalyzer(const char* code) {
    char token[100];
    int i = 0, j;

    printf("Tokens:\n");
    while (code[i] != '\0') {
        if (isalpha(code[i])) {  // Keywords or Identifiers
            j = 0;
            while (isalnum(code[i])) {
                token[j++] = code[i++];
            }
            token[j] = '\0';
            printf("Identifier/Keyword: %s\n", token);
        } else if (isdigit(code[i]) || code[i] == '.') {  // Numbers
            j = 0;
            while (isdigit(code[i]) || code[i] == '.') {
                token[j++] = code[i++];
            }
            token[j] = '\0';
            printf("Literal: %s\n", token);
        } else if (strchr("+-*/=();{}[],", code[i])) {  // Operators & Special Characters
            printf("Operator/Special: %c\n", code[i]);
            i++;
        } else if (code[i] == '"') {  // String Literals
            j = 0;
            token[j++] = code[i++];
            while (code[i] != '"' && code[i] != '\0') {
                token[j++] = code[i++];
            }
            if (code[i] == '"') {
                token[j++] = code[i++];
            }
            token[j] = '\0';
            printf("String Literal: %s\n", token);
        } else {
            i++;  // Skip whitespace and unrecognized characters
        }
    }
}

int main() {
    char code[1000];
    printf("Enter your code snippet (end input with ~):\n");
    fgets(code, sizeof(code), stdin);

    // Remove the '~' character at the end of the input
    char* ptr = strchr(code, '~');
    if (ptr != NULL) {
        *ptr = '\0';
    }

    lexicalAnalyzer(code);

    return 0;
}
