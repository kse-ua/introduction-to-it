using namespace std;
#include <iostream>
#include <map>


int addFunction(int a, int b) {
    auto result = a + b;
    return result;
}



int main() {
    cout << addFunction(10, 20) << " " << addFunction(1,2) << " ";
    cout << addFunction(100, 20) << " " << addFunction(100, 200) << endl;

}
