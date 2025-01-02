#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STATES 100
#define MAX_SYMBOLS 100

// Structure to hold the transition table
int transitionTable[MAX_STATES][MAX_SYMBOLS];

// Function to check if the input string is valid according to the DFA
int isValid(int noOfSymbol, const char inputSymbols[], int noOfState, int initialState, 
            const int acceptingStates[], int nAccect, const char inputString[]) {
    
    int currentState = initialState;
    int i = 0;

    // Loop through each character in the input string
    while (inputString[i] != '\0') {
        int symbolIndex = -1;
        
        // Find the index of the current symbol
        for (int j = 0; j < noOfSymbol; j++) {
            if (inputSymbols[j] == inputString[i]) {
                symbolIndex = j;
                break;
            }
        }

        // If the symbol is not valid, return false
        if (symbolIndex == -1) {
            return 0;
        }

        // Transition to the next state based on the current symbol
        currentState = transitionTable[currentState][symbolIndex];
        i++;
    }

    // Check if the final state is an accepting state
    for (int i = 0; i < nAccect; i++) {
        if (acceptingStates[i] == currentState) {
            return 1;
        }
    }

    return 0;
}

int main() {
    int nSymbol, nState, iniState, nAccect;
    char inputString[100];
    char inputSymbol[MAX_SYMBOLS];
    int acceptingState[MAX_STATES];

    // Input number of symbols
    printf("Enter number of symbols: ");
    scanf("%d", &nSymbol);

    // Input input symbols
    printf("Enter input symbols: ");
    scanf("%s", inputSymbol);

    // Input number of states
    printf("Enter number of states: ");
    scanf("%d", &nState);

    // Input initial state
    printf("Enter initial state: ");
    scanf("%d", &iniState);

    // Input number of accepting states
    printf("Enter number of accepting states: ");
    scanf("%d", &nAccect);

    // Input accepting states
    printf("Enter accepting states: ");
    for (int i = 0; i < nAccect; i++) {
        scanf("%d", &acceptingState[i]);
    }

    // Input the string to be validated
    printf("Enter input string: ");
    scanf("%s", inputString);

    // Populate the transition table
    for (int i = 0; i < nState; i++) {
        printf("Present State: '%d'\n", i);

        for (int j = 0; j < nSymbol; j++) {
            int nextState;
            printf("Enter the next state for input symbol '%c': ", inputSymbol[j]);
            scanf("%d", &nextState);
            transitionTable[i][j] = nextState;
        }
    }

    // Validate the input string
    if (isValid(nSymbol, inputSymbol, nState, iniState, acceptingState, nAccect, inputString)) {
        printf("The input string is valid.\n");
    } else {
        printf("The input string is invalid.\n");
    }

    return 0;
}
