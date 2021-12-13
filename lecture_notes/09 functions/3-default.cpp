#include <iostream>
 
int max(int x = 0, int y = 0) {
    if(x > y){
    return x;
  }
    if(y > x){
    return y;
  }
    if(y == x){
    return y;
  }
 }
int main() {
    std::cout << max(10, 20) << std::endl;
    std::cout << max(10) << std::endl;
    std::cout << max(-20) << std::endl;
 }
 
