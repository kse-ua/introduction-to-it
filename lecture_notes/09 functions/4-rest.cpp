#include <iostream>
using namespace std;

void PrintArrays (int arg[], int length) {
    for (int n=0; n<length; n++)
        cout << arg[n] << " ";
}

// There is no point to continue translating, 'cause we have already declared a type.

int main ()
{
    int FirstArray[] = {1, 2, 3};
    PrintArrays(FirstArray,3);
    return 0;
}
