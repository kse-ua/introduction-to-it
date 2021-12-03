#include <iostream>
#include <string>
using namespace std;

int main() {
  int ages[] = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };

  int first = ages[0];
  int length = sizeof(ages) / sizeof(ages[0]);
  int last = ages[length - 1];
  printf("first: %d\n", first);
  printf("last: %d\n", last);
  
  ages[4] = 4;
  printf("new element: %d\n", ages[4]);
  printf("function elements: %d\n");
  for(int i = 0; i < length; i++) {
      cout << ages[i] << "\n";
  }
}
