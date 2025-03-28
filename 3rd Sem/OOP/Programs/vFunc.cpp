#include <iostream>
using namespace std;

class base{
public:
    virtual void display(){
        cout << "Display from Base\n";
    }
    void print(){
        cout << "Print from Base";
    }
};
class derived : public base{
public:
    void display(){
        cout << "Display from Derived\n";
    }
    void print(){
        cout << "Print from Derived";
    }
};

int main(){
    base* b1 = new derived();
    b1->display();
    b1->print();
}