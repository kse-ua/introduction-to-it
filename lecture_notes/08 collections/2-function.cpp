#include <iostream>
using namespace std;

int printFirstLast(const int ages[], int length)
{
    int first = ages[0];
    int last = ages[length - 1];
    cout << "First element: " << first << endl;
    cout << "Last element: " << last << endl;
}

int main()
{
    int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};
    int length = sizeof(ages) / sizeof(int);
    printFirstLast(ages, length);
    return 0;
}
