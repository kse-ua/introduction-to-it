#include <iostream>
#include <stdio.h>
#include <stack>
using namespace std;

int main() {

    stack <int> ages;

    ages.push(10);
    ages.push(12);
    ages.push(15);
    ages.push(15);
    ages.push(17);
    ages.push(18);
    ages.push(18);
    ages.push(19);
    ages.push(20);
  
    ages.pop();

    while (!ages.empty()) {
      
        cout << ' ' << ages.top();
        ages.pop();
    }

    ages.push(20);

    while (!ages.empty()) {

        cout << ' ' << ages.top();
        ages.pop();

    }

}
