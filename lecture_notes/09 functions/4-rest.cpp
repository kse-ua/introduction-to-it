using namespace std;
#include <iostream>
#include <stdarg.h>

void catchRest(int length, ...)
{
     va_list args;
     va_start(args, length);
     for(int i = 0; i < length; i++)
     {
         int value = va_arg(args,int);
         cout << value << " ";
     }
     cout << endl;
     va_end(args);
}

void f2(int length, ...)
{
    va_list args;
    va_start(args, length);
    for(int i = 0; i < length; i++)
    {
        int value = va_arg(args, int);
        string type = typeid(value).name();
        cout << "Type: " << type << endl;
        cout << "Value: " << value << endl;
    }
    va_end(args);
}


int main()
{
    catchRest(3,1,2,3);
    f2(3,1,2,3);
}

