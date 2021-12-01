#include <iostream>
#include <stdio.h>
#include <stack>

int main() {
    
    std::stack<int> ages;
    
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
        std::cout << ' ' << ages.top();
        ages.pop();
    }
    
    ages.push(20);
    
    while (!ages.empty()) {
        std::cout << ' ' << ages.top();
        ages.pop();
    }
}
