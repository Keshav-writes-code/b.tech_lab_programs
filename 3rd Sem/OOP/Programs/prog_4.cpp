#include <iostream>
using namespace std;

// Define a structure to represent a phone number
struct Phone {
    int areaCode, exCode, number;
};

int main() {
    // Initialize a Phone structure with default values
    Phone p1{91, 83072, 92567};
    Phone p2;

    // Prompt the user to enter their phone number details
    cout << "\nEnter Your area code, exchange code, and number: ";
    cin >> p2.areaCode >> p2.exCode >> p2.number;

    // Display the phone numbers
    cout << "\nMy Number is (" << p1.areaCode << ") " << p1.exCode << "-" << p1.number;
    cout << "\nYour Number is (" << p2.areaCode << ") " << p2.exCode << "-" << p2.number << endl << endl;

    return 0;
}
