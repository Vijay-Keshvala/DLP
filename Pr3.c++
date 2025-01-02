#include <iostream>
#include <fstream>
#include <cctype>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

// Define sets for keywords, operators, and separators
const unordered_set<string> keywords = {"void", "struct", "int", "float", "long", "return"};
const unordered_set<char> operators = {'+', '-', '*', '/', '=', '%'};
const unordered_set<char> separators = {'(', ')', '{', '}', '[', ']', ',', ';'};

// Function to check if a string is a number
bool isNumber(const string &s) {
    for (char c : s) {
        if (!isdigit(c) && c != '.') return false;
    }
    return true;
}

// Function to classify tokens
void classifyToken(const string &token) {
    if (token.empty()) return;

    if (keywords.find(token) != keywords.end()) {
        cout << "Keyword: " << token << endl;
    } else if (isNumber(token)) {
        cout << "Number: " << token << endl;
    } else {
        cout << "Identifier: " << token << endl;
    }
}

// Lexical analyzer function
void lexicalAnalysis(const string &code) {
    string token;

    for (size_t i = 0; i < code.size(); ++i) {
        char c = code[i];

        // Handle separators
        if (separators.find(c) != separators.end()) {
            classifyToken(token);
            token.clear();
            cout << "Separator: " << c << endl;
        } 
        // Handle operators
        else if (operators.find(c) != operators.end()) {
            classifyToken(token);
            token.clear();
            cout << "Operator: " << c << endl;
        } 
        // Handle whitespace
        else if (isspace(c)) {
            classifyToken(token);
            token.clear();
        } 
        // Handle alphanumeric characters
        else {
            token += c;
        }
    }

    // Classify any remaining token
    classifyToken(token);
}

int main() {
    // Input C-like code from the user
    string code;
    cout << "Enter the C-like code (end with EOF):\n";
    while (getline(cin, code)) {
        lexicalAnalysis(code);
    }

    return 0;
}