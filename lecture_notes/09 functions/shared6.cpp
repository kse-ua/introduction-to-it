#include <iostream>
#include <map>
using namespace std;

int addFunction(int x, int y) {
    int result = x + y;
    return result;
}

map <string, int> cacheForAdd = {};
map <string, int> cacheForSub = {};

int addProcedure(int x, int y) {
    string key = to_string(x) + ',' + to_string(y);
    if (cacheForAdd.count(key) == 1) {
        return cacheForAdd[key];
    }
    else{
        int result = x + y;
        cacheForAdd[key] = result;
        return result;
    }
}

int subProcedure(int x, int y) {
    string key = to_string(x) + ',' + to_string(y);
    if (cacheForSub.count(key) == 1) {
        return cacheForSub[key];
    }
    else{
        int result = x - y;
        cacheForSub[key] = result;
        return result;
    }
}

int main() {
    cout << subProcedure(10, 20) << " ";
    cout << subProcedure(100, 200) << " ";
    cout << subProcedure(1, 2) << " ";
    cout << subProcedure(10, 20) << " ";
    cout << addProcedure(10, 20) << " ";
    cout << addProcedure(100, 200) << " ";
    cout << addProcedure(1, 2) << " ";
    cout << addProcedure(10, 20) << " ";
}