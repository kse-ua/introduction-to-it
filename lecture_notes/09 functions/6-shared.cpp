#include <iostream>  
#include <string>  
#include <map>
using namespace std;  

map <string, int> cache;

int addProcedure(int a, int b) {
    string key = to_string(a) + ", " +to_string(b);
    int res;
    cache.insert(pair <string, int>(key, res)); // meed to understand if it correct
    if (cache.empty()) {
        res = a + b;
        cache.insert(pair <string, int>(key, res));
        };
    return res;
}

int subProcedure(int a, int b) {
    string key = to_string(a) + ", " +to_string(b);
    int res = cache[key];
    if (res) { // actually has no meaning
        return res;
        }
    res = a - b;
    cache[key] = res;
    return res;
}

int main() {
    printf("sub: %d\n", subProcedure(5, 2));
    printf("add: %d\n", addProcedure(5, 2));  
}

// the code is actually not working properly