using namespace std;

#include <iostream>

template<class... Args>

void catchRest(Args... args)
{

    (cout << ... << args) << endl;
}


int main() {
    catchRest(1, 2, 3);
    int one = 1;
    char two = 'Hello';
    cout << typeid(one).name() << endl;
    cout << typeid(two).name() << endl;
}
