#include <iostream>
using namespace std;

struct date
{
    int day;
    int month;
    int year;
};

class HospitalDB
{
private:
    char **names;
    date **admit;
    char **disease;
    date **dischrg;
    int pCount;

public:
    HospitalDB() : pCount(0){};
    ~HospitalDB();
    void enterInfo(int pCount);
    void display();
};

void HospitalDB::enterInfo(int pCount)
{
    this->pCount = pCount;

    names = new char *[pCount];
    admit = new date *[pCount];
    disease = new char *[pCount];
    dischrg = new date*[pCount];

    for (int i = 0; i < pCount; i++)
    {
        names[i] = new char[30];
        admit[i] = new date;
        disease[i] = new char[100];
        dischrg[i] = new date;

        cout << endl << i + 1 << " Patient Details";
        // Name
        cout << "\nName :- ";
        cin >> names[i];

        // Date of Admission
        cout << "Admission Date (YYYY MM DD) :- ";
        cin >> admit[i]->year>>admit[i]->month>>admit[i]->day;

        // Disease
        cout << "Disease :- ";
        cin >> disease[i];

        // Date of Discharge
        cout << "Discharge Date (YYYY MM DD) :- ";
        cin >> dischrg[i]->year>>dischrg[i]->month>>dischrg[i]->day;
    }
}

HospitalDB::~HospitalDB()
{
    for (int i = 0; i < pCount; i++)
    {
        delete[] names[i];
    }
    delete[] names;
}

void HospitalDB::display()
{
    for (int i = 0; i < pCount; i++)
    {
        cout << "\n\n"<< i + 1 << ". Patient Details";
        
        cout << "\nName :- ";
        for (int j = 0; names[i][j] != '\0'; j++){
            cout << names[i][j];
        }

        cout << "\nDate of Admission :- ";
        cout<<admit[i]->day<<"/"<<admit[i]->month<<"/"<<admit[i]->year;
    
        cout << "\nDisease :- ";
        for (int j = 0; disease[i][j] != '\0'; j++){
            cout << disease[i][j];
        }

        cout << "\nDate of Discharge :- ";
        cout<<dischrg[i]->day<<"/"<<dischrg[i]->month<<"/"<<dischrg[i]->year;
    
    }
}

int main()
{
    HospitalDB db1;

    cout << "---Enter Data of Patients---\n";

    db1.enterInfo(2);
    cout << "\n---Displaying Data of Patients---";

    db1.display();

    return 0;
}