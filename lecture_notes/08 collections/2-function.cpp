#include <iostream>
using namespace std;

int get_first_and_last(int array[9]) {
  int first = array[0];
  int length = sizeof(array[9]) / sizeof(int);
  int last = array[length - 1];
  
  printf("first: %d\n", first);
  printf("last: %d\n", last);
}

int ages[] = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };


int main() {
  int result = get_first_and_last(ages[9])
  printf("result: %d\n", result);
}
