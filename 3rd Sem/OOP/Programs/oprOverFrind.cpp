#include <iostream>
using namespace std;

class myClass{
private:
    int data;

public:
    myClass() : data(0) {}
    myClass(int a) : data(a) {}
    void display(){
        cout<<"Data : "<<data;
    }
    friend myClass operator+(myClass ob1, myClass ob2);
};

myClass operator+(myClass ob1, myClass ob2){
    myClass ob3;
    ob3.data = ob1.data + ob2.data;
    return ob3;
}

int main(){
    myClass ob1(10), ob2(20), ob3;
    ob3 = ob1 + ob2;
    ob3.display();
}