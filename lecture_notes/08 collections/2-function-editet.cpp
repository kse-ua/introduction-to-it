#include <iostream>
#include <string>

void sumarray(int length,int array1[]){
    int first = array1[0];
    int last = array1[length-1];
    std::cout << "First: ";
    printf("%d",first);
    std::cout << " ";
    std::cout << "Last: ";
    printf("%d",last);
  }
int main() {
  int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};
  int length = sizeof(ages) / sizeof(int);
  sumarray(length,ages);

}
