#include <iostream>
using namespace std;

int max(int a = 0, int b = 0)
{
    return a > b ? a : b;
}

int main()
{
   cout << max(10, 20) << " " << max(10) << " " << max(-20);
}