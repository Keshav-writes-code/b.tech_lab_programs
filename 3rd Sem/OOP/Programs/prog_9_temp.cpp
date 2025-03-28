#include <iostream>
using namespace std;

// Structure to store date information
struct Date {
    int year;
    int month;
    int day;
};

// Base class to store patient information
class Patient {
protected:
    string name;
    Date admissionDate;
    string disease;
    Date dischargeDate;

public:
    // Function to enter patient information
    void enterInformation() {
        cout << "Enter patient name: ";
        cin >> name;

        cout << "Enter admission date (YYYY MM DD): ";
        cin >> admissionDate.year >> admissionDate.month >> admissionDate.day;

        cout << "Enter disease: ";
        cin >> disease;

        cout << "Enter discharge date (YYYY MM DD): ";
        cin >> dischargeDate.year >> dischargeDate.month >> dischargeDate.day;
    }

    // Function to display patient information
    void displayInformation() const {
        cout << "Name: " << name << endl;
        cout << "Admission Date: " << admissionDate.year << "-" << admissionDate.month << "-" << admissionDate.day << endl;
        cout << "Disease: " << disease << endl;
        cout << "Discharge Date: " << dischargeDate.year << "-" << dischargeDate.month << "-" << dischargeDate.day << endl;
    }
};

// Derived class to store the age of patients
class PediatricPatient : public Patient {
private:
    int age;

public:
    // Function to enter age information for pediatric patients
    void enterAge() {
        cout << "Enter patient age: ";
        cin >> age;
    }

    // Function to display age information for pediatric patients
    void displayAge() const {
        cout << "Age: " << age << " years" << endl;
    }

    // Function to get age for comparison
    int getAge() const {
        return age;
    }

    // Function to display information for pediatric patients
    void displayPediatricInformation() const {
        displayInformation();
        displayAge();
        cout << endl;
    }
};

int main() {
    const int maxPatients = 100; // Choose a suitable maximum number of patients
    PediatricPatient pediatricPatients[maxPatients];

    int numPatients;
    cout << "Enter the number of patients: ";
    cin >> numPatients;

    // Enter information for each patient
    for (int i = 0; i < numPatients && i < maxPatients; ++i) {
        PediatricPatient patient;
        patient.enterInformation();
        patient.enterAge();
        pediatricPatients[i] = patient;
    }

    // Display information for all patients
    cout << "\nList of all patients:\n";
    for (int i = 0; i < numPatients && i < maxPatients; ++i) {
        pediatricPatients[i].displayPediatricInformation();
    }

    // Display information for pediatric patients (less than twelve years in age)
    cout << "\nList of pediatric patients (less than twelve years in age):\n";
    for (int i = 0; i < numPatients && i < maxPatients; ++i) {
        if (pediatricPatients[i].getAge() < 12) {
            pediatricPatients[i].displayPediatricInformation();
        }
    }

    return 0;
}
