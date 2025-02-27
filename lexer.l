%{
#include <stdio.h>
%}

KEYWORD       "int"|"char"|"return"|"void"|"main"
IDENTIFIER    [a-zA-Z_][a-zA-Z0-9_]*
CONSTANT      [0-9]+
STRING        \"([^\\\"]|\\.)*\"|'([^\\']|\\.)*\'
OPERATOR      [+\-*/=]
PUNCTUATION   [(){};,]
WHITESPACE    [ \t\n]+
COMMENT       \/\/.*|\/\*([^*]|\*+[^*/])*\*+\/

%%

{KEYWORD}     { printf("Keyword: %s\n", yytext); }
{IDENTIFIER}  { printf("Identifier: %s\n", yytext); }
{CONSTANT}    { printf("Constant: %s\n", yytext); }
{STRING}      { printf("String: %s\n", yytext); }
{OPERATOR}    { printf("Operator: %s\n", yytext); }
{PUNCTUATION} { printf("Punctuation: %s\n", yytext); }
{WHITESPACE}  { /* Ignore whitespace */ }
{COMMENT}     { /* Ignore comments */ }
.             { printf("Invalid lexeme: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error opening file");
            return 1;
        }
        yyin = file;
    }

    yylex(); // Start the lexical analysis

    if (argc > 1) {
        fclose(yyin);
    }

    return 0;
}
int yywrap() {
    return 1;
}
