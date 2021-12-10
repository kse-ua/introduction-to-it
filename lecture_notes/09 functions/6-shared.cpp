#include <iostream>
#include <map>
using namespace std;

int subProcedure(int a, int b) {

    map <string, int> cache;
    std::string keyValue = std::to_string(a) + "," + std::to_string(b);
    if (cache.empty())
        int res = 0;
    int res = a - b;
    cache[keyValue] = res;
    return res;
}

int addProcedure(int a, int b) {

    map <string, int> cache;
    std::string keyValue = std::to_string(a) + "," + std::to_string(b);
    if (cache.empty())
        int res = 0;
    int res = a + b;
    cache[keyValue] = res;
    return res;
}

int main ()
{
    cout << "addProcedure: " << addProcedure(10, 20) << endl;
    cout << "addFunction: " << subProcedure(10, 20) << endl;
    cout << "addProcedure: " << addProcedure(100, 20) << endl;
    cout << "addFunction: " << subProcedure(100, 20) << endl;
    return 0;
}