#include <iostream>
#include <cmath>
using namespace std;

class DM {
    int meter, centiMeter;
public:
    DM(int m = 0, int cm = 0) : meter(m), centiMeter(cm) {}
    int getM() const { return meter; }
    int getCm() const { return centiMeter; }
    void setM(int m) { meter = m; }
    void setCm(int cM) { centiMeter = cM; }
    void display() const { cout << "\nMeter :- " << meter << "\nCentimeter :- " << centiMeter; }
    friend DM add(DM dm, class DB db);
};

class DB {
    int feet, inches;
public:
    DB(int f = 0, int inc = 0) : feet(f), inches(inc) {}
    int getF() const { return feet; }
    int getIn() const { return inches; }
    void setF(int f) { feet = f; }
    void setIn(int In) { inches = In; }
    void display() const { cout << "\nFeet :- " << feet << "\nInches :- " << inches; }
    friend DM add(DM dm, DB db);
};

DM add(DM dm1, DB db1) {
    return {dm1.getM() + round(db1.getF() * 0.305), dm1.getCm() + round(db1.getIn() * 2.54)};
}

DB add(DB db1, DM dm1) {
    return {static_cast<int>(db1.getF() + round(dm1.getM() * 3.28)), 
            static_cast<int>(db1.getIn() + round(dm1.getCm() * 0.305))};
}

int main() {
    int meter, cMeter, feet, Inches;
    cout << "\nEnter the first Distance\nIn meter, Centimeter: ";
    cin >> meter >> cMeter;

    cout << "\nEnter the Second Distance\nIn Feet, Inches: ";
    cin >> feet >> Inches;

    DM dm1(meter, cMeter);
    DB db1(feet, Inches);

    int oFrmt;
    cout << "\n1. Meter, Centimeter\n2. Feet, Inches\nEnter the Output format: ";
    cin >> oFrmt;

    cout << "\nSum of Values in ";
    if (oFrmt == 1) {
        auto dm2 = add(dm1, db1);
        cout << "Meter, Centimeter\n";
        dm2.display();
    } else if (oFrmt == 2) {
        auto db2 = add(db1, dm1);
        cout << "Feet, Inches\n";
        db2.display();
    } else {
        cout << "\nError: Invalid input";
    }
    cout << "\n\n";

    return 0;
}
