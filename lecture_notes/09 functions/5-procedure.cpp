using namespace std;
#include <iostream>
#include <map>

int addFunction(int a, int b);
int addProcedure(int a, int b);

map<string, int> cache;

int main(){
    cout << addFunction(10, 20) << " " << addFunction(1,2) << " ";
    cout << addFunction(100, 20) << " " << addFunction(100, 200) << endl;
    cout << addProcedure(10, 20) << " " << addProcedure(1,2) << " ";
    cout << addProcedure(100, 20) << " " << addProcedure(100, 200) << endl;
}

int addFunction(int a, int b){
    int res = a + b;
    return res;
}

int addProcedure(int a, int b){
    string key = to_string(a) + ',' + to_string(b);
    if (cache.count(key) == 1)
    {
        return cache[key];
    }
    int res = a + b;
    cache[key] = res;
    return res;
}

