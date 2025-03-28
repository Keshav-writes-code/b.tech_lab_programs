#include <iostream>
using namespace std;

// Define a structure called point
struct Point {
    int x;
    int y;
};

int main() {
    // Declare three points
    Point p1, p2, sumPoint;

    // User input for the first point
    cout << "\nEnter coordinates for P1: ";
    cin >> p1.x >> p1.y;

    // User input for the second point
    cout << "\nEnter coordinates for P2: ";
    cin >> p2.x >> p2.y;

    // Calculate the sum of the points
    sumPoint.x = p1.x + p2.x;
    sumPoint.y = p1.y + p2.y;

    // Display the result
    cout << "\nCoordinates of P1 + P2 are: " << sumPoint.x << ", " << sumPoint.y << endl<<endl;

    return 0;
}
