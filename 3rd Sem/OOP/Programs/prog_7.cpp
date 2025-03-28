#include <iostream>
using namespace std;

class Father {
protected:
    int age;

public:
    virtual void iam() {
        cout << "I am the father, my age is: " << age << endl;
    }
};

class Son : public Father {
public:
    Son(int x){age = x;}
    void iam() override {
        cout << "I am the son, my age is: " << age << endl;
    }
};

class Daughter : public Father {
public:
    Daughter(int x) {age = x;}
    void iam() override {
        cout << "I am the daughter, my age is: " << age << endl;
    }
};

int main() {
    Father* s1 = new Son(10);
    Father* d1 = new Daughter(10);

    s1->iam();
    d1->iam();
    delete s1;
    delete d1;
}
