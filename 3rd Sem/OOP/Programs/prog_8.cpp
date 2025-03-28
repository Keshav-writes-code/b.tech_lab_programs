#include <iostream>
#include <fstream>
using namespace std;

// Structure to store student data
struct Student{
    int rollNo;
    char name[31]; // 30 characters for the name + 1 for null terminator
    float marks;
};

int main()
{
    cout << "\nEnter number of Students :- ";
    int sCount;
    cin >> sCount;

    ofstream file("Students.bin", ios::binary);

    for (int i = 0; i < sCount; i++){
        cout << "\nEnter Details of ";

        Student s1;
        cout <<"Student - "<< i+1<<endl;
        cout << "Name :- ";
        cin >> s1.name;
        cout << "Roll No :- ";
        cin >> s1.rollNo;
        cout << "Marks :- ";
        cin >> s1.marks;

        file.write(reinterpret_cast<const char*>(&s1), sizeof(s1));
        if (!file) {
            cerr << "Error writing to file." << endl;
            return 1;
        }
    }
}