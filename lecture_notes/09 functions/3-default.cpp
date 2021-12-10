#include <iostream>
using namespace std;

int maximum(int a = 0, int b = 0)
{
    if (a > b) {
        return a;
    }

    if (b > a) {
        return b;
    }
    return 0;
}


int main()
{
    cout << maximum(-20) << '\n';
    return 0;
}
