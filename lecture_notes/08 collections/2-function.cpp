using namespace std;
#include <iostream>
int* getFirstLast(int array[], int length)
{
    int firstLast[2] = {array[0], array[length - 1]};
    return firstLast;
}

int main() {
    int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};
    int length = sizeof(ages)/sizeof(int);
    int first = getFirstLast(ages, length)[0];
    int last = getFirstLast(ages, length)[1];
    cout << "First element: "<< first << endl;
    cout << "Last element: "<< last << endl;
}
