%{
#include <stdio.h>
#include <ctype.h>

int length = 0, has_lower = 0, has_upper = 0, has_digit = 0, has_special = 0;
%}

%%
[a-z]      { has_lower = 1; length++; }
[A-Z]      { has_upper = 1; length++; }
[0-9]      { has_digit = 1; length++; }
[*;#$@]    { has_special = 1; length++; }
.|\n       { length++; }

%%

int main() {
    yylex();
    if (length >= 9 && length <= 15 && has_lower && has_upper && has_digit && has_special)
        printf("Valid password\n");
    else
        printf("Invalid password\n");
    return 0;
}

int yywrap() {
    return 1;
}
