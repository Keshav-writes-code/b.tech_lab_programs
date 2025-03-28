#include<iostream>
using namespace std;

class recevier
{
private:
    int data;
public:
    recevier() : data(0) {}
    void getdata(int a){
        data = a;
        cout<<a;
    }
};

class sender
{
private:
    int data;
    recevier* r1;
public:
    sender() : data(10), r1(nullptr) {};
    sender(int a) : data(a) {};
    void sendMsg(recevier* a){
        r1 = a;
        r1->getdata(data);
    }

};

int main (){
    sender s1(12345);
    recevier r1;
    int n;
    cin>>n;
    s1.sendMsg(&r1);
}