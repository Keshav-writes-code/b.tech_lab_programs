#include<iostream>
using namespace std;

class employee{
    protected:
        float sal;
        char name[50];
};
class manager:public employee{
    protected:
        char dep[30];
    public:
        void getData();
        void display();
};

void manager::getData()
{
    cout<<"Enter name: ";
    cin>>name;
    cout<<"Enter department: ";
    cin>>dep;
     cout<<"Enter salary: ";
    cin>>sal;
}

void manager::display()
{
    cout<<"Name: "<<name<<endl;
    cout<<"Salary: "<<sal<<endl;
    cout<<"Department: "<<dep<<endl;
}

class executive:public manager
{
    public:  
        void display(manager m)
        {
            cout<<"Executive: "<<endl;
            m.display();
        }
};
int main()
{
  
    manager m1;
    m1.getData();
    executive e;
    m1.display();
    e.display(m1);
}