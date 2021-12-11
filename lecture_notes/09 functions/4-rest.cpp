using namespace std;
#include <iostream>
#include <stdarg.h> 

void catchRest(int length, ...)
{
     va_list args;
     va_start(args, length);
     for (int i = 0; i < length; i++) {
         int value = va_arg(args, int);
         cout << value << " ";
     }
     cout << endl;
     va_end(args);
}

int main() {
    catchRest(4, 4, 6, 3, 7);
    // it makes no sense to get the type of args as we declare it alresdy
}
