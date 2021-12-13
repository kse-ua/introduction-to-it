#include <iostream>
using namespace std;

int Maximum(int a = 0, int b = 0) {
    if (a > b) return a;
    return b;
}


int main()
{
    cout << Maximum(-20) << '\n';
    return 0;
}
