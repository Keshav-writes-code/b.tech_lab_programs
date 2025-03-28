#include <iostream>
using namespace std;

int main() {
    char doAnother;

    do {
        // Variables for user input
        double num1, num2, result;
        char op;

        // User input for the calculation
        cout << "\nEnter expression: ";
        cin >> num1 >> op >> num2;

        // Perform the specified arithmetic operation using a switch statement
        switch (op) {
            case '+': result = num1 + num2; break;
            case '-': result = num1 - num2; break;
            case '*': result = num1 * num2; break;
            case '/': result = (num2 != 0) ? num1 / num2 : (cout << "Error: Division by zero!" << endl, 0);
                     break;
            default: cout << "Invalid operator!" << endl; return 1;
        }

        // Display the result
        cout << "Answer = " << result << endl;

        // Ask if the user wants to do another calculation
        cout << "\nDo another (Y/N)? ";
        cin >> doAnother;

    } while (doAnother == 'Y' || doAnother == 'y');
    cout<<endl;
    return 0;
}