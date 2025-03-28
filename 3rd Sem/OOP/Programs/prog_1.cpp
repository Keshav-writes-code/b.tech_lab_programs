#include<iostream>
using namespace std;

// Function to calculate n raised to the power p (default: 2)
double power(double n, int p = 2) {
    double result = 1.0;
    for (int i = 0; i < p; ++i) result *= n;
    return result;
}

int main() {

    // Get input values from the user
    double base; int exponent;
    cout << "\nEnter base (n): "; cin >> base;
    cout << "\nEnter exponent (p, default: 2): "; cin >> exponent;

    // Calculate and display the result
    cout <<endl<< base << " ^ " << exponent << " = " << power(base, exponent) << endl<<endl;
    return 0;
}