#include <iostream>
#include <vector>
#include <string>
using namespace std;


int f(char s[])
{
    int length = sizeof(s) / sizeof(char);
    return length;
}

int f1(char s[]) {
    int length = sizeof(s) / sizeof(char);
    return length;
}

void f1() {
    char cities[][7] = {'Athens', 'Roma'};
}

int main() {
    char cities[][16] = {'Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga'};
    return 0;
}
