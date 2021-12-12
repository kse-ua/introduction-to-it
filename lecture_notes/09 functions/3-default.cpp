#include <iostream>
using namespace std;

int max(int a = 0, int b = 0) {
    int larger = (a > b) ? a : b;
}
int main()
{
    cout << max(20,10) << endl;
    cout << max(10, 20) << endl;
    cout << max(-20) << endl;
}
