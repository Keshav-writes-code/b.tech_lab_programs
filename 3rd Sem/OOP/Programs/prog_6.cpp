#include <iostream>
#include <cmath>
using namespace std;

class Rational {
    double num, denom;

public:
    Rational() : num(0), denom(1) {}
    Rational(double num, double denom) : num(num), denom(denom) {}

    void reduce() {
        double a = num, b = denom;
        while (b != 0) {
            double temp = b;
            b = fmod(a, b);
            a = temp;
        }
        num /= a;
        denom /= a;
    }

    void display() const {
        cout << num << "/" << denom;
    }

    Rational operator+(const Rational &r) const {
        Rational temp;
        temp.num = r.num * denom + num * r.denom;
        temp.denom = r.denom * denom;
        temp.reduce();
        return temp;
    }

    friend ostream &operator<<(ostream &output, const Rational &r) {
        output << r.num << "/" << r.denom;
        return output;
    }

    friend istream &operator>>(istream &input, Rational &r) {
        cout << "Enter Numerator: ";
        input >> r.num;
        cout << "Enter Denominator: ";
        input >> r.denom;
        r.reduce();
        return input;
    }
};

int main() {
    cout << "Program to Process Rational Numbers\n\n";

    Rational r1, r2;

    cout << "Enter 1st Rational Number:\n";
    cin >> r1;

    cout << "\nEnter 2nd Rational Number:\n";
    cin >> r2;

    cout << "\nFirst Rational Number: ";
    r1.display();
    cout << "\nSecond Rational Number: ";
    r2.display();

    Rational r3 = r1 + r2;
    cout << "\n\nSum of the two Rational Numbers (Reduced Form): " << r3;

    cout << endl << endl << endl;
    return 0;
}
