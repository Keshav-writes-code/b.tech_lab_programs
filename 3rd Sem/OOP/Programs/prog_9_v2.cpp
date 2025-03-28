#include <iostream>
using namespace std;

// Structure to represent a date
struct Date {
    int day, month, year;
};

// Base class representing a generic patient
class Patient {
protected:
    char name[30], disease[100];
    Date admit, discharge;

public:
    void enterInfo() {
        cout << "Name (without Spaces): "; cin >> name;
        cout << "Admission Date (YYYY MM DD): "; cin >> admit.year >> admit.month >> admit.day;
        cout << "Disease (without Spaces): "; cin >> disease;
        cout << "Discharge Date (YYYY MM DD): "; cin >> discharge.year >> discharge.month >> discharge.day;
    }

    void display() {
        cout << "\nName: " << name;
        cout << "\nAdmission Date: " << admit.day << "/" << admit.month << "/" << admit.year;
        cout << "\nDisease: " << disease;
        cout << "\nDischarge Date: " << discharge.day << "/" << discharge.month << "/" << discharge.year << endl;
    }
};

// Derived class representing a pediatric patient, inheriting from the base class
class Pediatric : public Patient {
private:
    int age;

public:
    void enterAge() { cout << "Age: "; cin >> age; }
    void displayAge() { cout << "Age: " << age << "\n"; }
    int getAge() { return age; }
};

int main() {
    cout << "\n--------------------------";
    cout << "\n----Hospital DB System----";
    cout << "\n--------------------------\n\n";

    int pCount;
    cout << "Enter No. of Patients: "; cin >> pCount;

    // Creating an array of Pediatric patients based on the user input
    Pediatric patients[pCount];
    for (int i = 0; i < pCount; i++) {
        Pediatric p1;
        cout << endl << i + 1 << ". Patient Details\n";
        p1.enterInfo();
        p1.enterAge();
        patients[i] = p1;
    }

    // Displaying information for all patients
    cout << "\n---- List of all the Patients ----\n";
    for (int i = 0; i < pCount; i++) {
        cout << endl << i + 1 << ". Patient Details";
        patients[i].display();
        patients[i].displayAge();
    }

    // Displaying information for pediatric patients (age < 12)
    cout << "\n---- List of Pediatric Patients ----\n";
    for (int i = 0; i < pCount; i++) {
        if (patients[i].getAge() < 12) {
            cout << endl << i + 1 << ". Patient Details";
            patients[i].display();
            patients[i].displayAge();
        }
    }

    return 0;
}