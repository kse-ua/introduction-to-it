#include <iostream>
using namespace std;

int maximum(int a = 0, int b = 0) {
    if (a > b) return a;
    return b;
}


int main()
{
    cout << maximum(-20) << '\n';
    return 0;
}
