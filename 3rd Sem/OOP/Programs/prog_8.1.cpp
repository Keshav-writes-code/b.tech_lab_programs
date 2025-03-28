#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

// Structure to store student data
struct Student {
    int rollNo;
    char name[31];  // 30 characters for the name + 1 for null terminator
    float marks;
};

int main() {
    int numStudents;

    cout << "Enter the number of students: ";
    cin >> numStudents;

    // Open a binary file for writing
    ofstream outFile("students.bin", ios::binary | ios::out);

    if (!outFile) {
        cerr << "Error opening file for writing." << endl;
        return 1;
    }

    for (int i = 0; i < numStudents; ++i) {
        Student student;

        cout << "\nEnter Roll No. for student " << i + 1 << ": ";
        cin >> student.rollNo;

        cout << "Enter Name for student " << i + 1 << " (30 characters or less): ";
        cin.ignore();  // Clear newline character from the buffer
        cin.getline(student.name, sizeof(student.name));

        cout << "Enter Marks for student " << i + 1 << ": ";
        cin >> student.marks;

        // Write the student data to the binary file
        outFile.write(reinterpret_cast<const char*>(&student), sizeof(Student));

        if (!outFile) {
            cerr << "Error writing to file." << endl;
            return 1;
        }
    }

    // Close the file
    outFile.close();

    cout << "Data written to students.dat successfully." << endl;

    return 0;
}
