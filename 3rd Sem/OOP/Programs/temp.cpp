#include <iostream>
#include <cmath>
using namespace std;

void reduce(double &num, double &denom)
{
    double prev_remmainder = num, current_remainder = denom;
    
    while (current_remainder != 0)
    {
        double temp = current_remainder;
        current_remainder = fmod(prev_remmainder, current_remainder);
        prev_remmainder = temp;
        cout<<"--------------\n";
        cout << "prev_remmainder" << prev_remmainder << endl;
        cout << "current_remainder" << current_remainder << endl;
    }

    num /= prev_remmainder;
    denom /= prev_remmainder;
}

int main()
{
    double a, b;
    cout<<"Enter 2 vals :- \n";
    cin>>a;
    cin>>b;
    reduce(a,b);

    cout<<a<<"/"<<b;
    return 0;
}
